from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

from tests.acceptance.page_model.registration_page import RegistrationPage

use_step_matcher('re')


@given('Esu Pagrindiniame puslapyje')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('Esu Prisijungimo puslapyje')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('Esu Registracijos puslapyje')
def step_impl(context):
    expected_url = RegistrationPage(context.driver).url
    assert context.driver.current_url == expected_url
