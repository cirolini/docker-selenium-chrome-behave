import time

@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)

@then('it should have a tag "{tag}"')
def step(context, tag):
   assert tag in context.browser.page_source


@when('field with name "{selector}" is given "{value}"')
def step(context, selector, value):
    elem = context.browser.find_element_by_name(selector)
    elem.send_keys(value)
    elem.submit()
    time.sleep(5)

@then('title becomes "{title}"')
def step(context, title):
    assert title in context.browser.title
