from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_blog_page import NewPostPage

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


@when('Ivedu "(.*)" i "(.*)" laukeli')
def step_imp(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('Paspaudziu "submit" mygtuka')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()


@then('Matau irasa kurio title yra "(.*)"')
def step_imp(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])


