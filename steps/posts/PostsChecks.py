import allure

from schemas.posts_schema import PostsSchema
from steps.posts.PostsSteps import PostsSteps


class PostsChecks(PostsSteps):
    @allure.step("Проверка ответа метода создания нового поста")
    def check_posts_response(
            self,
            response,
            user_id=None,
            body=None,
            title=None
    ):
        """
        :param response: ответ метода
        :param user_id: id пользователя
        :param body: текст поста
        :param title: заголовок поста
        """
        self.validate_response_body(PostsSchema(), response)
        if user_id is not None:
            assert response.get("userId") == user_id, \
                (
                    f"Значение user_id из ответа: {response.get("user_id")}"
                    f" не соответствует ожидаемому user_id: {user_id}"
                )
        if body is not None:
            assert response.get("body") == body, \
                (
                    f"Значение body из ответа: {response.get("body")}"
                    f" не соответствует ожидаемому body: {body}"
                )
        if title is not None:
            assert response.get("title") == title, \
                (
                    f"Значение title из ответа: {response.get("title")}"
                    f" не соответствует ожидаемому title: {title}"
                )
        return self

    @allure.step("Проверить значение id нового поста")
    def check_new_post_id(self, response):
        new_id = self.get_not_existed_post_id()
        assert response.get("id") == new_id, (
            f"Значение id нового поста: {response.get("id")} \n "
            f"не совпадает с ожидаемым: {new_id}"
        )
        return self

    @allure.step("Проверить значение id в ответе при обновлении поста")
    def check_post_id_after_update(self, response, post_id):
        """
        :param response: тело ответа
        :param post_id: id поста
        """
        assert response.get("id") == post_id, (
            f"Значение id поста: {response.get("id")} \n "
            f"не совпадает с ожидаемым: {post_id}"
        )
        return self

    @allure.step('Проверить пустой ответ после удаления поста')
    def check_response_after_delete(self, response, expected_response):
        """
        :param response: тело ответа
        :param expected_response: ожидаемое тело ответа
        """
        assert response == expected_response, "Ответ не пустой"
        return self
