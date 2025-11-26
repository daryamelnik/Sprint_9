import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.feature('Авторизация')
class TestLogin:
    
    @allure.title('Успешная авторизация')
    @allure.description('Проверка авторизации с валидными учетными данными')
    def test_login_success(self, driver, manual_user):
        import time
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        
        with allure.step('Переход на страницу входа'):
            driver.get("https://foodgram-frontend-1.prakticum-team.ru/signin")
            time.sleep(1)
        
        with allure.step('Заполнить все поля формы авторизации'):
            login_page.fill_login_form(
                manual_user["email"],
                manual_user["password"]
            )
        
        with allure.step('Нажать кнопку "Войти"'):
            login_page.click_login_button()
        
        with allure.step('Обработка возможного alert'):
            time.sleep(2)
            try:
                driver.switch_to.alert.accept()
            except:
                pass
        
        with allure.step('Ожидание перехода на главную страницу'):
            time.sleep(1)
            main_page.wait_for_url_contains("/recipes")
        
        with allure.step('Проверить переход на главную страницу'):
            current_url = main_page.get_current_url()
            assert "/recipes" in current_url or "/signin" not in current_url

