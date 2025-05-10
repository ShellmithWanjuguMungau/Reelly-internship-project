import time

from selenium.webdriver.common.by import By

from Pages.base_page import Page

class Settings(Page):
    SUPPORT_LNK=(By.CSS_SELECTOR, "[href*='whatsapp.com']")
    NEWS_LINK=(By.CSS_SELECTOR, "[href*='t.me']")

    def click_support_lnk(self):
        time.sleep(5)

        self.wait_until_clickable_click(*self.SUPPORT_LNK)

    def Verify_the_url_contains_whatsapplnk(self,expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def  Click_news_option(self):
        self.wait_until_clickable_click(*self.NEWS_LINK)

    def Verify_url_contains_telegramlink(self,expected_partial_url):
        self.verify_partial_url(expected_partial_url)