import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname, delete_courier, \
    login_and_get_id


class TestCourierLogin:

    @allure.title('Проверка успешной аутентификации курьера при вводе валидных данных')
    @allure.description('Проверяются код и тело ответа.')
    def test_courier_login_success(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        requests.post(Urls.URL_courier_create, data=payload)
        response = requests.post(Urls.URL_courier_login, data=payload)
        assert response.status_code == 200 and 'id' in response.text
        courier_id = login_and_get_id(payload)
        delete_courier(courier_id)

    @allure.title('Проверка получения ошибки аутентификации курьера при вводе невалидных данных')
    @allure.description('В тест по очереди передаются наборы данных с несуществующим логином или неверным паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка получения ошибки аутентификации курьера с пустым полем логина или пароля')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для входа'