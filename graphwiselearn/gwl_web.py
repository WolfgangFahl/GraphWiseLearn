"""
Created on 2024-05-21

@author: wf
"""
from nicegui import ui, Client
from ngwidgets.input_webserver import InputWebserver, InputWebSolution, WebserverConfig
from ngwidgets.llm import LLM
from ngwidgets.login import Login
from fastapi.responses import RedirectResponse
from graphwiselearn.version import Version
from graphwiselearn.gwl_generate import LearningView
from wikibot3rd.sso_users import Sso_Users

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
        self.users = Sso_Users(self.config.short_name)
        self.login = Login(self, self.users)
        self.llm=LLM()

        @ui.page("/user")
        async def show_user(client: Client):
            if not self.login.authenticated():
                return RedirectResponse("/login")
            return await self.page(client, GwlSolution.show_user)


        @ui.page("/login")
        async def login(client: Client) -> None:
            return await self.page(client, GwlSolution.show_login)


class GwlSolution(InputWebSolution):
    """
    Self assessment UI per client
    """

    def __init__(self, webserver: GwlWebServer, client: Client):
        super().__init__(webserver, client)  # Call to the superclass constructor
        self.llm=webserver.llm

    def configure_menu(self):
        """
        configure the menu
        """
        username = self.login.get_username()
        user = self.get_user()
        admin_flag = "🔑" if user and user.is_admin else ""
        self.link_button(f"{username}{admin_flag}", f"/user", "person")


    async def show_login(self):
        """Show login page"""
        await self.login.login(self)

    async def show_user(self):
        """
        show the currently logged in user
        """

        def show():
            user = self.get_user()
            _logout_button = ui.button("logout", icon="logout", on_click=self.logout)
            html_markup = f"""
    <h1>User Details</h1>
    <p><strong>ID:</strong> {user.id}</p>
    <p><strong>Name:</strong> {user.name}</p>
    <p><strong>Real Name:</strong> {user.real_name}</p>
    <p><strong>Email:</strong> {user.email}</p>
    <p><strong>Edit Count:</strong> {user.editcount}</p>
    """
            ui.html(html_markup)

        await self.setup_content_div(show)

    async def logout(self):
        await self.login.logout()

    def lwl_generate_page(self):
        """
        show the learning content generation interface
        """
        self.learning_view = LearningView(self)
        self.learning_view.setup()

    async def home(self):
        await self.setup_content_div(self.lwl_generate_page)