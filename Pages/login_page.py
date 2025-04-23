from selenium.webdriver.common.by import By

from Pages.base_page import Page

class LoginPage(Page):
    EMAIL_INPUT=(By.ID, "email-2")
    PASSWORD_INPUT=(By.CSS_SELECTOR, "[data-name='Password']")
    CONTINUE_BTN=(By.CSS_SELECTOR, "[class*='login-button']")

    def open_login_page(self):
        self.open_url(self.base_url+'sign-in')

    def Enter_email (self, email):
        self.input_text(email,*self.EMAIL_INPUT)

    def Enter_password (self, password):
        self.input_text(password,*self.PASSWORD_INPUT)

    def Click_continue(self):
        self.click(*self.CONTINUE_BTN)