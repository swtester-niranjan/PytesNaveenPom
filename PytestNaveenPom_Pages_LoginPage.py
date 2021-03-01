from selenium.webdriver.common.by import By
from Config.config import TestData

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        """self.driver.implicitly_wait(10)"""

    """Page actions"""
    """this is used to get page title"""

    def get_loginpage_title(self, title):
        return self.get_title(title)

    """this is check sign up link exists"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is to login in app"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
