import random
import string

import allure
import requests

from api.PostsApi import PostsApi
from request.post_request import PostRequest
from schemas.posts_schema import PostsRequestSchema


class PostsSteps(PostsApi):
    @allure.step("Создать новый пост")
    def create_new_post(
            self,
            user_id=None,
            title=None,
            body=None,
            status_code=requests.codes['created']
    ):
        """
        :param user_id: id пользователя
        :param title: заголовок поста
        :param body: текст поста
        :param status_code: ожидаемый код ответа
        """
        post_request = PostRequest(
            user_id=user_id,
            title=title,
            body=body
        )
        body = self.create_request(PostsRequestSchema(), post_request)
        response = self.post_new_posts(body, res_status=status_code)
        return response

    @allure.step("Обновить пост")
    def update_post(
            self,
            post_id,
            user_id=None,
            title=None,
            body=None,
            status_code=requests.codes['ok']
    ):
        """
        :param post_id: id поста
        :param user_id: id пользователя
        :param title: заголовок поста
        :param body: текст поста
        :param status_code: ожидаемый код ответа
        """
        post_request = PostRequest(
            user_id=user_id,
            title=title,
            body=body
        )
        body = self.create_request(PostsRequestSchema(), post_request)
        response = self.update_current_post(
            post_id=post_id,
            body=body,
            res_status=status_code)
        return response

    @allure.step('Получить существующий {param} поста')
    def get_existed_post_param(self, param):
        posts = self.get_all_posts()
        params = [user.get(param) for user in posts]
        random_value = random.choice(params)
        return random_value

    @allure.step("Получить не существующий id поста")
    def get_not_existed_post_id(self):
        posts = self.get_all_posts()
        id_posts = [post.get("id") for post in posts]
        post_id = id_posts[-1] + 1
        return post_id

    def get_random_text_for_post(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
