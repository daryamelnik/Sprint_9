from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_FORM = (By.TAG_NAME, "form")


class LoginPage(BasePage):
    def fill_login_form(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def is_login_form_visible(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_FORM)

