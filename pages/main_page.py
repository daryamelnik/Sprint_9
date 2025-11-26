from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[text()='Создать рецепт']")


class MainPage(BasePage):
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)
    
    def click_register_button(self):
        self.click_element(MainPageLocators.REGISTER_BUTTON)
    
    def is_logout_button_visible(self):
        return self.is_element_visible(MainPageLocators.LOGOUT_BUTTON)
    
    def click_create_recipe_link(self):
        self.click_element(MainPageLocators.CREATE_RECIPE_LINK)

