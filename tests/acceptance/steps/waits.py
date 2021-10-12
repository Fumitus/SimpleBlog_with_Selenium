from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


@given('Laukti kol puslapis uzsikraus, bet ne ilgaiu nei 5s')
def step_imp(context):
    WebDriverWait(context.driver, 6).until(
        expected_conditions.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)
    )
