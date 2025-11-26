from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    USERNAME_INPUT = (By.NAME, "username")
    FIRST_NAME_INPUT = (By.NAME, "first_name")
    LAST_NAME_INPUT = (By.NAME, "last_name")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")


class RegisterPage(BasePage):
    def fill_registration_form(self, email, password, username, first_name, last_name):
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)
        self.input_text(RegisterPageLocators.USERNAME_INPUT, username)
        self.input_text(RegisterPageLocators.FIRST_NAME_INPUT, first_name)
        self.input_text(RegisterPageLocators.LAST_NAME_INPUT, last_name)
    
    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

