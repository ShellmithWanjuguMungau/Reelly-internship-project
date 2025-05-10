from behave import given, when, then
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

SUPPORT_LNK = (By.CSS_SELECTOR, "[href*='whatsapp.com']")


@when('Click on the support option')
def click_on_support_option(context):
    wait = WebDriverWait(context.driver, 10)
    support_element =wait.until(EC.presence_of_element_located((SUPPORT_LNK)))

    context.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", support_element)
    context.app.settings_page.click_support_lnk()

@when('Switch to the new tab')
def switch_to_new_tab(context):
    context.current_tab=context.app.base_page.current_window_handle()
    context.app.base_page.switch_to_new_window()

@then ('Verify the url contains {whatsapplnk}')
def verify_url_contains_whatsapplnk(context, whatsapplnk):
    context.app.settings_page.Verify_the_url_contains_whatsapplnk(whatsapplnk)

    # headless testing screenshot
    time.sleep(5)
    context.driver.save_screenshot('Screenshots/whatsapppage.png')


@then("Switch back to previous page")
def Switch_to_Previous_Page(context):
    the_current_tab=context.current_tab
    context.app.base_page.switch_to_window_by_id(the_current_tab)


@then("Click on news option")
def click_on_news_option(context):
    context.app.settings_page.Click_news_option()


@then("Verify url contains {telegramlink}")
def verify_url_contains(context, telegramlink):
    context.app.settings_page.Verify_url_contains_telegramlink(telegramlink)

    # headless testing screenshot
    # time.sleep(5)
    context.driver.save_screenshot('Screenshots/telegrampage.png')
