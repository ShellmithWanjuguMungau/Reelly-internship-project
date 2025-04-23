from Pages.base_page import Page
from Pages.login_page import LoginPage
from Pages.header_page import Header
from Pages.settings_page import Settings

class Application(Page):
    def __init__(self, driver):
        self.driver = driver
        self.base_page=Page(driver)
        self.login_page=LoginPage(driver)
        self.header_page=Header(driver)
        self.settings_page=Settings(driver)