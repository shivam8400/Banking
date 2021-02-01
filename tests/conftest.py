import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")

def browserinvoke(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\HP\\Desktop\\geckodriver.exe")
    driver.get("http://www.way2automation.com/angularjs-protractor/banking/#/login")
    driver.maximize_window()
    print(driver.current_url)
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()
