"""
Created on 2023-11-03

@author: wf
"""

from ngwidgets.webserver_test import WebserverTest
from graphwiselearn.gwl_web import GwlWebServer
from graphwiselearn.gwl_cmd import GwlCmd

class TestGwlWebserver(WebserverTest):
    """
    test the GraphWiseLearn webserver
    """

    def setUp(self, debug=False, profile=True):
        server_class = GwlWebServer
        cmd_class = GwlCmd
        WebserverTest.setUp(self, server_class, cmd_class, debug=debug, profile=profile)

    def testDemoWebserver(self):
        """
        test API docs access
        """
        # self.debug=True
        html = self.getHtml("/docs")
        self.assertTrue("Swagger" in html)
