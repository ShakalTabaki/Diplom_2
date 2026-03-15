import allure
import pytest
from methods.user_methods import UserMethods
from generators import generate_user


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):

        user_data = generate_user()

        response = UserMethods.create_user(user_data)

        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self):

        user_data = generate_user()

        UserMethods.create_user(user_data)

        response = UserMethods.create_user(user_data)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"


    @allure.title("Нельзя создать пользователя без обязательного поля")
    @pytest.mark.parametrize(
        "missing_field",
        [
            "email",
            "password",
            "name"
        ]
    )
    def test_create_user_without_required_field(self, missing_field):

        user_data = generate_user()

        user_data.pop(missing_field)

        response = UserMethods.create_user(user_data)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

