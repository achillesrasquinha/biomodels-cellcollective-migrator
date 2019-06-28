# imports - module imports
from bcm.cli.parser import get_args
from bcm import cli

def cli_format(string, type_):
    args = get_args(as_dict = False)

    if not args.no_color:
        string = cli.format(string, type_)

    return string