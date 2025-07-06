import allure
import requests

from api.RestClient import RestClient


class UsersApi(RestClient):
    @allure.step("Получение списка пользователей: GET /users")
    def get_users(
            self,
            params=None,
            res_status=requests.codes['ok']
    ):
        """
        :param params: параметры запроса
        :param res_status: ожидаемый код ответа
        """
        return self.get(
            url="/users",
            params=params,
            status_code=res_status
        )

    @allure.step("Получение одного пользователя: GET /users/{user_id}")
    def get_user_by_id(
            self,
            user_id,
            res_status=requests.codes['ok']
    ):
        """
        :param user_id: id пользователя
        :param res_status: ожидаемый код ответа
        """
        return self.get(
            url=f"/users/{user_id}",
            status_code=res_status
        )
