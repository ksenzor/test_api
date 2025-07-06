import allure
import requests

from api.RestClient import RestClient


class PostsApi(RestClient):

    @allure.step("Создание нового поста: POST /posts")
    def post_new_posts(
            self,
            body=None,
            res_status=requests.codes['created']
    ):
        """
        :param body: тело запроса
        :param res_status: ожидаемый код ответа
        """
        return self.post(
            url="/posts",
            status_code=res_status,
            body=body)

    @allure.step("Обновление поста: PUT /posts/{post_id}")
    def update_current_post(
            self,
            post_id,
            body=None,
            res_status=requests.codes['ok']
    ):
        """
        :param post_id: id поста
        :param body: тело запроса
        :param res_status: ожидаемый код ответа
        """
        return self.put(
            url=f"/posts/{post_id}",
            status_code=res_status,
            body=body
        )

    @allure.step("Удаление поста: DELETE /posts/{post_id}")
    def delete_post(
            self,
            post_id,
            res_status=requests.codes['ok']
    ):
        """
        :param post_id: id поста
        :param res_status: ожидаемый код ответа
        """
        return self.delete(
            url=f"/posts/{post_id}",
            status_code=res_status
        )

    @allure.step("Получение списка постов: GET /posts")
    def get_all_posts(
            self,
            res_status=requests.codes['ok']
    ):
        """
        :param res_status: ожидаемый код ответа
        """
        return self.get(
            url="/posts",
            status_code=res_status
        )
