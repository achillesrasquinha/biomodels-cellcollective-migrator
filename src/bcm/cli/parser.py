# imports - standard imports
import argparse

# imports - module imports
from bcm.__attr__     import (
    __name__,
    __version__,
    __description__,
    __command__
)
from bcm.util.environ  import getenv
from bcm.cli           import util as _cli
from bcm.cli.formatter import ArgumentParserFormatter

_DESCRIPTION_JUMBOTRON = \
"""
%s (v %s)

%s
""" % (
    _cli.format(__name__,        _cli.RED),
    _cli.format(__version__,     _cli.BOLD),
    _cli.format(__description__, _cli.BOLD)
)

def get_parser():
    parser = argparse.ArgumentParser(
        prog            = __command__,
        description     = _DESCRIPTION_JUMBOTRON,
        add_help        = False,
        formatter_class = ArgumentParserFormatter
    )
    parser.add_argument("-q", "--biomodels-query",
        action  = "append",
        help    = "Query to be used for BioModels"
    )
    parser.add_argument("-s", "--size",
        default = 100,
        help    = "Size of results to be fetched."
    )
    parser.add_argument("-p", "--publish",
        action  = "store_true",
        help    = "Publish after import"
    )
    parser.add_argument("-y", "--yes",
        action  = "store_true",
        help    = "Confirm for all dialogs."
    )
    parser.add_argument("-c", "--check",
        action  = "store_true",
        help    = "Check for outdated packages."
    )
    # parser.add_argument("-l", "--latest",
    #     action  = "store_true",
    #     help    = "Update all packages to latest."
    # )
    parser.add_argument("-i", "--interactive",
        action  = "store_true",
        help    = "Interactive Mode"
    )
    parser.add_argument("--cc-email",
        help     = "Cell Collective Email",
        default  = getenv("CC_EMAIL"),
    )
    parser.add_argument("--cc-password",
        help    = "Cell Collective Password",
        default = getenv("CC_PASSWORD")
    )
    # parser.add_argument("--no-cache",
    #     action  = "store_true",
    #     help    = "Avoid fetching latest updates from PyPI server."
    # )
    parser.add_argument("--no-color",
        action  = "store_true",
        help    = "Avoid colored output."
    )
    parser.add_argument("-V", "--verbose",
        action  = "store_true",
        help    = "Display verbose output."
    )
    parser.add_argument("-v", "--version",
        action  = "version",
        version = __version__,
        help    = "Show %s's version number and exit." % __name__
    )
    parser.add_argument("-h", "--help",
        action  = "help",
        default = argparse.SUPPRESS,
        help    = "Show this help message and exit."
    )

    return parser

def get_args(args = None, known = True, as_dict = True):
    parser  = get_parser()

    if known:
        args, _ = parser.parse_known_args(args)
    else:
        args    = parser.parse_args(args)

    if as_dict:
        args = args.__dict__
        
    return args