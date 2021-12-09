from pytest_bdd import scenarios, when, then, given, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios

scenarios("../features/duckDuckGo.feature")

# Shared Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)
# When Steps

@when('the user searches for python')
def search_phrase(browser):
    search_input = browser.find_element(By.ID, 'search_form_input_homepage')
    search_input.send_keys("python" + Keys.RETURN)
