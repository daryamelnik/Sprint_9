from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RecipePageLocators:
    NAME_INPUT = (By.NAME, "name")
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    TIME_INPUT = (By.NAME, "cooking_time")
    DESCRIPTION_INPUT = (By.NAME, "text")
    INGREDIENT_INPUT = (By.XPATH, "//input[@placeholder='Выберите ингредиент']")
    INGREDIENT_DROPDOWN = (By.CLASS_NAME, "styles_selectList__gHOTT")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[@placeholder='Количество']")
    CREATE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_CARD = (By.CLASS_NAME, "card")
    RECIPE_TITLE = (By.CLASS_NAME, "recipe_title")


class RecipePage(BasePage):
    def fill_recipe_name(self, name):
        self.input_text(RecipePageLocators.NAME_INPUT, name)
    
    def upload_image(self):
        image_path = Path(__file__).parent.parent / "test_image.jpg"
        image_input = self.find_element(RecipePageLocators.IMAGE_INPUT)
        image_input.send_keys(str(image_path.absolute()))
    
    def fill_cooking_time(self, time):
        self.input_text(RecipePageLocators.TIME_INPUT, time)
    
    def fill_description(self, description):
        self.input_text(RecipePageLocators.DESCRIPTION_INPUT, description)
    
    def add_ingredient(self, ingredient_name, amount):
        self.input_text(RecipePageLocators.INGREDIENT_INPUT, ingredient_name)
        
        self.wait.until(EC.visibility_of_element_located(RecipePageLocators.INGREDIENT_DROPDOWN))
        
        ingredient_option = (By.XPATH, f"//div[contains(@class, 'styles_selectList__gHOTT')]//div[contains(text(), '{ingredient_name}')]")
        self.click_element(ingredient_option)
        
        self.input_text(RecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
    
    def click_create_button(self):
        self.click_element(RecipePageLocators.CREATE_BUTTON)
    
    def is_recipe_card_visible(self):
        return self.is_element_visible(RecipePageLocators.RECIPE_CARD)
    
    def get_recipe_title(self):
        return self.get_element_text(RecipePageLocators.RECIPE_TITLE)

