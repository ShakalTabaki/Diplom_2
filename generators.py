import random
import string


def generate_user():
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    name = ''.join(random.choices(string.ascii_lowercase, k=8))

    return {
        "email": email,
        "password": password,
        "name": name
    }
