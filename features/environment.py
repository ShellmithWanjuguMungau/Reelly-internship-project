from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from support.logger import logger
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from app.application import Application


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    #Chrome driver
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    #Mobile emulation
    # mobile_emulation = { "deviceName": "Nexus 5" }
    # mobile_emulation = {"deviceName": "iPad Mini"}
    mobile_emulation = {"deviceName": "Surface Duo"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)



    #Firefox driver
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # ## HEADLESS MODE ####
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080") #screenshots saved
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )
    #

    # ### BROWSERSTACK ###
    # bs_user = 'shellytest_D1tdGe'
    # bs_key = '7CWxNz9grwiAxQr8Jyk4'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "deviceName": "iPhone 15 Pro",
    #     "osVersion": "17",
    #     "realMobile": "true",
    #     "browserName": "Safari",
    #     "sessionName": scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app=Application(context.driver)



def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: , {scenario.name}')
    print('\nStarted scenario: ', scenario.name)

    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step:  {step.name}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.warning(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()
