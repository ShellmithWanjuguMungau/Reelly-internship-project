from selenium.webdriver.common.by import By

from Pages.base_page import Page

class Header(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "[class*='settings-link']")

    def open_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS_BTN)

