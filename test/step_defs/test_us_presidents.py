import requests
from pytest_bdd import scenarios, given, then, parsers

url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"

scenarios('../features/us_presidents.feature')

@given(parsers.parse('The DuckDuckGo API is queried with "presidents of the united states"'))

@then(parsers.parse('the response status code is "200"'))
def duckduckgo_response_code(ddg_response, code):
    assert ddg_response.status_code == code

@then('the response contains results for "Presidents of the United States"')
def duckduckgo_response_heading():
    response = requests.get(url)
    my_jason = response.json()
    headings = my_jason['Heading']
    assert "Presidents of the United States" in headings
    assert len(headings) == 31

@then('the response contains results for "Related Topics"')
def duckduckgo_response_content():
    response = requests.get(url)
    my_jason = response.json()
    r_topics = my_jason['RelatedTopics']
    assert len(r_topics) == 50

@then('the response contains last name "Adams"')
def test_ddg2():
    response = requests.get(url)
    my_jason = response.json()
    r_topics = my_jason['Adams']
    assert "Adams" in r_topics
