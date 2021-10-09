from behave import *

use_step_matcher('re')


@when('paspaudziu mygtuka Blog id "(.*)"')
def step_imp(context, link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()
