import pytest
from selenium import webdriver

#По выбору:
#Запускать: pytest -s -v --browser_name=chrome test_parser.py
#def pytest_addoption(parser):
#    parser.addoption('--browser_name', action='store', default=None,
#                     help="Choose browser: chrome or firefox")

#По умолчанию chrome:
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

#Язык страницы:
#def pytest_addoption(parser):
#    parser.addoption('--language', action='store', default=None,
#                 help="Choose browser: language")

#@pytest.fixture(scope="function")
#def browser(request):
#    user_language = request.config.getoption("language")
#    print("\nstart chrome browser for test..")
#    options = Options()
#    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#    browser = webdriver.Chrome(options=options)
#    yield browser
#    print("\nquit browser..")
#    browser.quit()


#from selenium import webdriver
#import pytest

#@pytest.fixture(scope="function")
#def browser():
#    print("\nstart browser for test..")
#    browser = webdriver.Chrome()
#    yield browser
#    print("\nquit browser..")
#    browser.quit()