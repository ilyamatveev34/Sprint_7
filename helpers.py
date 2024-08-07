import requests
from faker import Faker
from urls import Urls

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_login():
    login = fake.text(max_nb_chars=7) + str(fake.random_int(0, 999))
    return login


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_firstname():
    first_name = fakeRU.first_name()
    return first_name


def login_and_get_id(payload):
    response = requests.post(Urls.URL_courier_login, json=payload)
    courier_id = response.json().get('id')
    return courier_id


def delete_courier(courier_id):
    response = requests.delete(f'{Urls.URL_courier_create}/{courier_id}')
    assert response.status_code == 200