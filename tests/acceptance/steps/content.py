from behave import *
import time
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('Puslapyje yra rodomas prisijungimo mygtukas "(.*)"')
def step_imp(context, content):
    page = BlogPage(context.driver)
    assert page.login_button.text == content


@then('Puslapyje yra rodomas registracijos mygtukas "(.*)"')
def step_imp(context, content):
    page = BlogPage(context.driver)
    assert page.registration_button.text == content



