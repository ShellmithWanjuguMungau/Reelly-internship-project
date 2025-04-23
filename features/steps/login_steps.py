from selenium.webdriver.common.by import By
from behave import given, when, then


@given ('Open login page')
def open_login_page (context):
    context.app.login_page.open_login_page()


@given("Enter email")
def Enter_email(context):
    context.app.login_page.Enter_email('testshelly29@gmail.com')


@given("Enter password")
def Enter_password(context):
    context.app.login_page.Enter_password('Test@123')


@given("Click continue")
def click_continue(context):
    context.app.login_page.Click_continue()