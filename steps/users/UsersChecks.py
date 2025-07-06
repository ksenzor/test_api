import allure

from data.tests_constants import EXPECTED_USERS_DATA
from schemas.users_schema import UsersSchema
from steps.users.UsersSteps import UsersSteps


class UsersChecks(UsersSteps):
    @allure.step('Проверка структуры ответа метода получения информации о пользователях')
    def check_users_response_structure(self, response):
        for user in response:
            self.validate_response_body(UsersSchema(), user)
        return self

    @allure.step('Проверка содержимого ответа метода получения информации о пользователях')
    def check_users_response_data(self, response):
        assert response == EXPECTED_USERS_DATA, (
            f"Фактический результат: {response} \n "
            f"не совпадает с ожидаемым: {EXPECTED_USERS_DATA}"
        ) # т.к. отсутствует доступ к БД, сравнение осуществляется с константой
        return self

    @allure.step('Проверить, что значение, переданное в фильтре, присутствует в ответе')
    def check_users_filtered_response_data(
            self,
            filter_name,
            filter_value,
            response
    ):
        """
        :param filter_name: наименование параметра для фильтрации
        :param filter_value: значение, переданное в параметре
        :param response: ответ метода
        """
        assert filter_value == response[0][filter_name], (
            f"Значение фильтра: {filter_value} \n "
            f"отсутствует в ответе: {response}"
        )
        return self

    @allure.step('Проверка ответа метода получения информации о пользователе')
    def check_user_response(self, response, user_id):
        """
        :param response: тело ответа
        :param user_id: id пользователя
        """
        self.validate_response_body(UsersSchema(), response)
        assert response == EXPECTED_USERS_DATA[user_id - 1], (
            f"Фактический результат: {response} \n "
            f"не совпадает с ожидаемым: {EXPECTED_USERS_DATA[0].get(user_id)}"
        )
        return self

    @allure.step('Проверить ответ при ошибке')
    def check_error_response(self, response, expected_response):
        """
        :param response: тело ответа
        :param expected_response: ожидаемое тело ответа
        """
        assert response == expected_response, "Ответ не пустой"
        return self
