"""
Created on 2024-05-21

@author: wf
"""
import sys

from ngwidgets.cmd import WebserverCmd

from graphwiselearn.gwl_web import GwlWebServer


class GwlCmd(WebserverCmd):
    """
    Command line for self GraphWiseLearn
    """


def main(argv: list = None):
    """
    main call
    """
    cmd = GwlCmd(
        config=GwlWebServer.get_config(),
        webserver_cls=GwlWebServer,
    )
    exit_code = cmd.cmd_main(argv)
    return exit_code


DEBUG = 0
if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-d")
    sys.exit(main())
