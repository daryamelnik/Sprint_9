import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_data import TestData
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    return options


@pytest.fixture
def driver(chrome_options):
    selenium_host = os.environ.get('SELENIUM_HOST', 'localhost')
    selenium_port = os.environ.get('SELENIUM_PORT', '4444')
    
    if selenium_host != 'localhost':
        driver = webdriver.Remote(
            command_executor=f'http://{selenium_host}:{selenium_port}/wd/hub',
            options=chrome_options
        )
    else:
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(0)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(TestData.BASE_URL)
    return MainPage(driver)


@pytest.fixture
def user_data():
    return TestData.generate_user_data()


@pytest.fixture
def registered_user(driver, user_data):
    import time
    driver.get(TestData.BASE_URL)
    main_page = MainPage(driver)
    main_page.click_register_button()
    
    register_page = RegisterPage(driver)
    register_page.fill_registration_form(
        user_data["email"],
        user_data["password"],
        user_data["username"],
        user_data["first_name"],
        user_data["last_name"]
    )
    register_page.click_register_button()
    
    time.sleep(1)
    
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    
    time.sleep(1)
    
    return user_data


@pytest.fixture
def manual_user():
    return {
        "email": TestData.MANUAL_USER_EMAIL,
        "password": TestData.MANUAL_USER_PASSWORD,
        "username": TestData.MANUAL_USER_USERNAME
    }


@pytest.fixture
def authorized_user(driver, manual_user):
    import time
    
    driver.get(TestData.BASE_URL + "/signin")
    time.sleep(1)
    
    login_page = LoginPage(driver)
    
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    
    login_page.fill_login_form(
        manual_user["email"],
        manual_user["password"]
    )
    
    time.sleep(0.5)
    
    login_page.click_login_button()
    
    time.sleep(2)
    
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    
    time.sleep(1)
    
    return driver

