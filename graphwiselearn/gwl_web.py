"""
Created on 2024-05-21

@author: wf
"""
from nicegui import ui, Client
from ngwidgets.input_webserver import InputWebserver, InputWebSolution, WebserverConfig

from graphwiselearn.version import Version


class GwlWebServer(InputWebserver):
    """
    nicegui based web server for GraphWiseLearn
    """

    @classmethod
    def get_config(cls) -> WebserverConfig:
        """
        get the configuration for this Webserver
        """
        copy_right = "(c)2024 Wolfgang Fahl"
        config = WebserverConfig(
            short_name="gwl",
            copy_right=copy_right,
            version=Version(),
            default_port=9863,
        )
        server_config = WebserverConfig.get(config)
        server_config.solution_class = GwlSolution
        return server_config

    def __init__(self):
        """Constructs all the necessary attributes for the WebServer object."""
        InputWebserver.__init__(self, config=GwlWebServer.get_config())


class GwlSolution(InputWebSolution):
    """
    Self assessment UI per client
    """

    def __init__(self, webserver: GwlWebServer, client: Client):
        super().__init__(webserver, client)  # Call to the superclass constructor
