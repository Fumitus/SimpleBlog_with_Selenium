from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')


@when('Paspaudziu nuoroda "(.*)"')
def step_imp(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()
