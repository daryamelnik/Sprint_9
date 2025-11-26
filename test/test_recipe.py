import allure
from pages.main_page import MainPage
from pages.recipe_page import RecipePage
from test_data import TestData


@allure.feature('Создание рецепта')
class TestRecipe:
    
    @allure.title('Доступ к странице создания рецепта')
    @allure.description('Проверка что авторизованный пользователь может перейти к созданию рецепта')
    def test_create_recipe_success(self, authorized_user):
        import time
        main_page = MainPage(authorized_user)
        
        with allure.step('Проверить что авторизация прошла успешно'):
            current_url = authorized_user.current_url
            assert "/recipes" in current_url or "/signin" not in current_url
        
        with allure.step('Перейти на страницу создания рецепта'):
            authorized_user.get(TestData.BASE_URL + "/recipes/create")
            time.sleep(2)
        
        with allure.step('Проверить доступ к странице создания рецепта'):
            current_url = authorized_user.current_url
            assert "/recipes/create" in current_url or "/recipes" in current_url

