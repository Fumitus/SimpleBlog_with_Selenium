from behave import *

from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@then('Puslapyje yra rodoma antraste')
def step_imp(context):
    page = HomePage(context.driver)
    assert page.title.is_displayed()


@step('Puslapio antraste yra "(.*)"')
def step_imp(context, content):
    page = HomePage(context.driver)
    assert page.title.text == content
