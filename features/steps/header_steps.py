
from behave import given, when, then

@when('Click on the settings option')
def click_settings(context):
    context.app.header_page.open_settings()
