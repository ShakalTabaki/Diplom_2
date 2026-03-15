import requests
import allure
from urls import Urls


class UserMethods:

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(payload):
        return requests.post(Urls.REGISTER, json=payload)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(payload):
        return requests.post(Urls.LOGIN, json=payload)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(
            f"{Urls.BASE_URL}/api/auth/user",
            headers={"Authorization": token}
        )
