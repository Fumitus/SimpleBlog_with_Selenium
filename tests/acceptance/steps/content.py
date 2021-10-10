from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')


@then('Puslapuje yra rodoma antraste')
def step_imp(context):
    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert title_tag.is_displayed()


@step('Puslapio antraste yra "(.*)"')
def step_imp(context, content):
    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert title_tag.text == content
