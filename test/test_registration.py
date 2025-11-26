import allure
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from test_data import TestData


@allure.feature('Регистрация')
class TestRegistration:
    
    @allure.title('Успешное создание аккаунта')
    @allure.description('Проверка создания нового аккаунта с валидными данными')
    def test_create_account_success(self, main_page, user_data):
        with allure.step('Нажать кнопку "Создать аккаунт"'):
            main_page.click_register_button()
        
        register_page = RegisterPage(main_page.driver)
        
        with allure.step('Заполнить все поля формы регистрации'):
            register_page.fill_registration_form(
                user_data["email"],
                user_data["password"],
                user_data["username"],
                user_data["first_name"],
                user_data["last_name"]
            )
        
        with allure.step('Нажать кнопку "Создать аккаунт"'):
            register_page.click_register_button()
        
        login_page = LoginPage(main_page.driver)
        
        with allure.step('Обработка возможного alert'):
            try:
                main_page.driver.switch_to.alert.accept()
            except:
                pass
        
        with allure.step('Ожидание перехода на страницу авторизации'):
            login_page.wait_for_url_contains("/signin")
        
        with allure.step('Проверить переход на страницу авторизации'):
            assert "/signin" in login_page.get_current_url()
        
        with allure.step('Проверить отображение формы авторизации'):
            assert login_page.is_login_form_visible()

