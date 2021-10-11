import json

from behave import *
import time
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@when('Paspaudziu mygtuka "Registruotis"')
def step_imp(context):
    page = BlogPage(context.driver)
    page.registration_button_1.click()
