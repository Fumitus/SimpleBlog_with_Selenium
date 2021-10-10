from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('Esu Home puslapyje')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('http://127.0.0.1:5000')


@given('Esu Blog puslapyje')
def step_impl(context):
    context.browser = webdriver.Firefox()
    context.browser.get('http://127.0.0.1:5000/blog')


@then('Atsidaro Blog puslapis')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url


@then('Atsidaro Home puslapis')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url
