import allure
from methods.order_methods import OrderMethods


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self):

        ingredients_response = OrderMethods.get_ingredients()

        ingredients = ingredients_response.json()["data"]

        ingredient_ids = [
            ingredients[0]["_id"],
            ingredients[1]["_id"]
        ]

        order_data = {
            "ingredients": ingredient_ids
        }

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title("Нельзя создать заказ без ингредиентов")
    def test_create_order_without_ingredients(self):

        order_data = {
            "ingredients": []
        }

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 400


    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user):

        user_data, access_token = create_user

        ingredients_response = OrderMethods.get_ingredients()
        ingredients = ingredients_response.json()["data"]

        ingredient_ids = [
            ingredients[0]["_id"],
            ingredients[1]["_id"]
        ]

        order_data = {
            "ingredients": ingredient_ids
        }

        response = OrderMethods.create_order(order_data, access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):

        ingredients_response = OrderMethods.get_ingredients()
        ingredients = ingredients_response.json()["data"]

        ingredient_ids = [
            ingredients[0]["_id"],
            ingredients[1]["_id"]
        ]

        order_data = {
            "ingredients": ingredient_ids
        }

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title("Нельзя создать заказ с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):

        order_data = {
            "ingredients": ["123invalidhash"]
        }

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 500
