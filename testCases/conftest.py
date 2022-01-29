from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        s = Service("D:/Selenium Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("Chrome Browser opened")
    elif browser == 'firefox':
        s = Service("D:/Selenium Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=s)
        print("Firefox Browser opened")
    else:
        s = Service("D:/Selenium Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    return driver


# Will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


# Will return browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Raja"


# Hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


