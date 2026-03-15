import allure
import pytest
from methods.user_methods import UserMethods


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):

        user_data, access_token = create_user

        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }

        response = UserMethods.login_user(login_data)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()


    @allure.title("Нельзя залогиниться с неверным логином или паролем")
    @pytest.mark.parametrize(
        "email,password",
        [
            ("wrong_email@mail.com", "123456"),
            ("", "wrong_password")
        ]
    )
    def test_login_with_invalid_credentials(self, create_user, email, password):

        user_data, access_token = create_user

        login_data = {
            "email": email if email else user_data["email"],
            "password": password
        }

        response = UserMethods.login_user(login_data)

        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
