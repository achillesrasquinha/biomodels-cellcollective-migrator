# imports - standard imports
import sys, os, os.path as osp
import re
import json
import tempfile as tf

# imports - module imports
from bcm.commands.util import cli_format
from bcm.table         import Table
from bcm.util.string   import pluralize, ellipsis
from bcm.util.environ  import getenvvar
from bcm 		       import request as req, cli, log
from bcm.__attr__      import __name__
from bcm.api           import biomodels as bmapi, CCAPI

logger = log.get_logger(level = log.DEBUG)

@cli.command
def command(
	biomodels_query     = [ ],
	size                = 100,
	publish				= False,
	cc_email            = None,
	cc_password         = None,
	latest				= False,
	check		 		= False,
	interactive  		= False,
	yes			 		= False,
	no_cache            = False,
	no_color 	 		= True,
	verbose		 		= False
):
	ccapi = CCAPI(cc_email, cc_password)

	if not verbose:
		logger.setLevel(log.NOTSET)
		
	cli.echo(cli_format("Checking...", cli.YELLOW))
	logger.info("Arguments Passed: %s" % locals())

	models = [ ]
	table  = Table(header = ["No.", "Name"])

	if biomodels_query:
		for query in biomodels_query:
			logger.info("Searching Models for query: %s" % query)
			results = bmapi.search(query, size = size)
			
			for model in results["models"]:
				id_   = model["id"]
				model = bmapi.model(id_)
				files = model["files"]
				
				for f in files["additional"]:
					if f["name"].endswith("xml"):
						models.append({
							"id": id_,
							"name": model["name"],
							"filename": f["name"]
						})

						table.insert([
							cli_format(len(table) + 1, cli.YELLOW),
							ellipsis(model["name"], threshold = 100)
						])

	string  = table.render()

	cli.echo(string)
	cli.echo()

	nmodels = len(models)

	smodels = pluralize("model", nmodels) # Models "string"
	query   = "Do you wish to import %s %s?" % (nmodels, smodels)

	if nmodels and (yes or interactive or cli.confirm(query, quit_ = True)):
		errstr = '%s not found. Use %s or the environment variable "%s" to set value.'

		if not cc_email:
			raise ValueError(errstr % ("Cell Collective Email",    "--cc-email", 	getenvvar("CC_EMAIL")))
		if not cc_password:
			raise ValueError(errstr % ("Cell Collective Password", "--cc-password", getenvvar("CC_PASSWORD")))

		ccapi = CCAPI(cc_email, cc_password)

		for model in models:
			with tf.TemporaryDirectory() as tempdir:
				filename = osp.join(tempdir, "%s.sbml" % model["id"])

				with open(filename, "wb") as f:
					cli.echo(cli_format("Downloading Model %s..." % model["name"], cli.YELLOW))

					for chunk in bmapi.model_download(model["id"], model["filename"]):
						f.write(chunk)

				cli.echo(cli_format("Importing Model %s..." % model["name"], cli.YELLOW))
				if ccapi.import_model(filename, save = True):
					cli.echo(cli_format("Model %s successfully imported." % model["name"], cli.GREEN))