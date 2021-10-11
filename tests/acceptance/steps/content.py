from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@then('Puslapuje yra rodoma antraste')
def step_imp(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('Puslapio antraste yra "(.*)"')
def step_imp(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content
