#Generic class that is the blueprint has all methods all classes can re-use

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Page: #will call selenium actions
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://soft.reelly.io/'
        self.wait= WebDriverWait(self.driver, 15)

    def open_url(self,url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator) :
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        current_handles = self.driver.window_handles
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print("All windows:", all_windows)
        print("switching to new window:", all_windows[-1])
        self.driver.switch_to.window(all_windows[-1])

    def switch_to_window_by_id(self,window_id):
        print("switching to new window:",window_id)
        self.driver.switch_to.window(window_id)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator), message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element(locator), message=f'Element still visible by {locator}'
        )

    def verify_text(self, expected_text, *locator):
        actual_text=self.driver.find_element(*locator).text
        assert actual_text == expected_text ,f'{expected_text} did not match {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text} not found in {actual_text}'


    def verify_url (self, expected_url):
        # current_url = self.driver.current_url
        # print(f'Current url: {current_url}')
        # assert expected_url == current_url, f'Expected url {expected_url} but got {current_url}'
        self.wait.until(EC.url_to_be(expected_url), message=f'URL does not match {expected_url} ')

    def verify_partial_url (self, expected_partial_url):
        current_url = self.driver.current_url
        print(current_url)

        # assert expected_partial_url in current_url, f'Expected url {expected_partial_url} not found in {current_url}'
        self.wait.until(EC.url_contains(expected_partial_url), message=f'{current_url} does not contain {expected_partial_url} ')

    def close(self):
        self.driver.close()