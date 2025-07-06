import random

import allure
import requests

from data.tests_constants import INVALID_DATA_FOR_PARAMS, EMPTY_DICT, EMPTY_LIST
from steps.users.UsersChecks import UsersChecks


@allure.epic("Тесты для проверки методов users")
class TestUsers:
    @allure.title("Метод: GET /users. Проверка ответа "
                  "без передачи параметров для фильтрации")
    def test_get_all_users(self):
        users = UsersChecks().get_users()
        (UsersChecks()
         .check_users_response_structure(users)
         .check_users_response_data(users))

    @allure.title("Метод: GET /users. Проверка ответа с"
                  " корректными значениями параметров для фильтрации")
    def test_get_users_with_filters(self):
        params = {
            'id': UsersChecks().get_existed_user_param("id"),
            'name': UsersChecks().get_existed_user_param("name"),
            'username': UsersChecks().get_existed_user_param("username"),
            'email': UsersChecks().get_existed_user_param("email"),
            'phone': UsersChecks().get_existed_user_param("phone"),
            'website': UsersChecks().get_existed_user_param("website")
        }
        for param, value in params.items():
            users = UsersChecks().get_users(params=[(param, value)])
            UsersChecks().check_users_response_structure(users)
            UsersChecks().check_users_filtered_response_data(
                filter_name=param,
                filter_value=value,
                response=users
            )

    @allure.title("Метод: GET /users. Проверка ответа с"
                  " некорректными значениями параметров для фильтрации")
    def test_get_users_with_incorrect_filters(self):
        # Проверка передачи некорректных значений
        params = {
            'id': random.choice(INVALID_DATA_FOR_PARAMS),
            'name': random.choice(INVALID_DATA_FOR_PARAMS),
            'username': random.choice(INVALID_DATA_FOR_PARAMS),
            'email': random.choice(INVALID_DATA_FOR_PARAMS),
            'phone': random.choice(INVALID_DATA_FOR_PARAMS),
            'website': random.choice(INVALID_DATA_FOR_PARAMS)
        }
        for param, value in params.items():
            response = UsersChecks().get_users(params=[(param, value)])
            UsersChecks().check_error_response(response, EMPTY_LIST)

        # Проверка передачи в параметре части валидного значения
        params = {
            'name': UsersChecks().get_part_param_value("name"),
            'username': UsersChecks().get_part_param_value("username"),
            'email': UsersChecks().get_part_param_value("email"),
            'phone': UsersChecks().get_part_param_value("phone"),
            'website': UsersChecks().get_part_param_value("website")
        }
        for param, value in params.items():
            response = UsersChecks().get_users(params=[(param, value)])
            UsersChecks().check_error_response(response, EMPTY_LIST)


    @allure.title("Метод: GET /users/[id]. Проверка ответа при передаче валидного id")
    def test_get_user_by_id(self):
        user_id = UsersChecks().get_existed_user_param("id")
        users = UsersChecks().get_user_by_id(user_id)
        UsersChecks().check_user_response(users, user_id)

    @allure.title("Метод: GET /users/[id]. Проверка ошибки, при передаче невалидного id")
    def test_error_user_by_id(self):
        # Проверка id, которого нет в БД
        not_exist_user_id = UsersChecks().get_not_existed_user_id()
        response = UsersChecks().get_user_by_id(
            not_exist_user_id,
            requests.codes["not_found"]
        )
        UsersChecks().check_error_response(response, EMPTY_DICT)

        # Проверка невалидных значний id
        for value in INVALID_DATA_FOR_PARAMS:
            response = UsersChecks().get_user_by_id(
                value,
                requests.codes["not_found"]
            )
            UsersChecks().check_error_response(response, EMPTY_DICT)
