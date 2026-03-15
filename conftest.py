import pytest

from generators import generate_user
from methods.user_methods import UserMethods


@pytest.fixture
def create_user():

    user_data = generate_user()

    response = UserMethods.create_user(user_data)
    access_token = response.json()["accessToken"]

    yield user_data, access_token

    UserMethods.delete_user(access_token)
