import random
import string
import time


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email():
    timestamp = int(time.time() * 1000)
    random_part = generate_random_string(5)
    return f"test_{timestamp}_{random_part}@example.com"


def generate_unique_username():
    timestamp = int(time.time() * 1000)
    random_part = generate_random_string(3)
    return f"user{timestamp}{random_part}"


class TestData:
    BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru"
    
    VALID_PASSWORD = "TestPass123!@#"
    VALID_FIRST_NAME = "Test"
    VALID_LAST_NAME = "User"
    
    MANUAL_USER_EMAIL = "darya.melnik000@gmail.com"
    MANUAL_USER_PASSWORD = "2DJfz6zXsicCaVH"
    MANUAL_USER_USERNAME = "darya.melnik000@gmail.com"
    
    RECIPE_TIME = "30"
    RECIPE_DESCRIPTION = "This is a test recipe description"
    INGREDIENT_NAME = "абрикосовое варенье"
    INGREDIENT_AMOUNT = "100"
    
    @staticmethod
    def generate_user_data():
        return {
            "email": generate_unique_email(),
            "password": TestData.VALID_PASSWORD,
            "username": generate_unique_username(),
            "first_name": TestData.VALID_FIRST_NAME,
            "last_name": TestData.VALID_LAST_NAME
        }
    
    @staticmethod
    def generate_recipe_name():
        return f"Test Recipe {generate_random_string(5)}"

