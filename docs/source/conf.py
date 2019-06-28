import sys
import os, os.path as osp
import datetime as dt

def pardir(path, level = 1):
    for _ in range(level):
        path = osp.dirname(path)
    return path

BASEDIR = osp.abspath(pardir(__file__, 2))
NOW     = dt.datetime.now()

sys.path.insert(0, BASEDIR)

import bcm

project   = bcm.__name__
author    = bcm.__author__
copyright = "%s %s" % (NOW.year, bcm.__author__)

version   = bcm.__version__
release   = bcm.__version__

source_suffix  = ".md"
source_parsers = { ".md": "recommonmark.parser.CommonMarkParser" }

master_doc     = "index"