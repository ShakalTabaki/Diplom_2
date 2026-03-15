import requests
import allure
from urls import Urls


class OrderMethods:

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(data, token=None):

        headers = {}

        if token:
            headers = {"Authorization": token}

        return requests.post(
            Urls.ORDERS,
            json=data,
            headers=headers
        )
