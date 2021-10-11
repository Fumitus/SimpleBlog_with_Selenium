from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@given('Esu Home puslapyje')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('Esu Blog puslapyje')
def step_impl(context):
    context.driver = webdriver.Firefox()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('Atsidaro Blog puslapis')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('Atsidaro Home puslapis')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
