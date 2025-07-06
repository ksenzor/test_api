import random

import allure
import requests

from data.tests_constants import EMPTY_DICT, INVALID_DATA_FOR_PARAMS, EMPTY_STR
from steps.posts.PostsChecks import PostsChecks
from steps.users.UsersChecks import UsersChecks


@allure.epic("Тесты для проверки методов posts")
class TestPosts:
    @allure.title("Метод: POST /posts. Проверка создания нового поста со всеми параметрами")
    def test_create_new_full_post(self):
        user_id = UsersChecks().get_existed_user_param("id")
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(1, 100)))
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().create_new_post(
            user_id=user_id,
            title=title,
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id,
            title=title,
            body=body
        )
         .check_new_post_id(response))

    @allure.title("Метод: POST /posts. Проверка создания нового поста с частью параметров")
    def test_create_new_partial_post(self):
        # Проверка создания поста только с user_id
        user_id = UsersChecks().get_existed_user_param("id")
        response = PostsChecks().create_new_post(
            user_id=user_id
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id
        )
         .check_new_post_id(response))
        # Проверка создания поста только с title
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().create_new_post(
            title=title
        )
        (PostsChecks()
         .check_posts_response(
            response,
            title=title
        )
         .check_new_post_id(response))
        # Проверка создания поста только с body
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().create_new_post(
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            body=body
        )
         .check_new_post_id(response))

    @allure.title("Метод: POST /posts. Проверка создания нового поста с несуществующим user_id")
    def test_create_new_post_incorrect_user_id(self):
        user_id = UsersChecks().get_not_existed_user_id()
        response = PostsChecks().create_new_post(
            user_id=user_id
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id
        )
         .check_new_post_id(response))

    @allure.title("Метод: POST /posts. Проверка создания нового поста с объемными title и body")
    def test_create_new_large_post(self):
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(4000, 4001)))
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(4000, 4001)))
        response = PostsChecks().create_new_post(
            title=title,
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            title=title,
            body=body
        )
         .check_new_post_id(response))

    @allure.title("Метод: POST /posts. Проверка создания нового поста без параметров title, body, userId")
    def test_create_new_empty_post(self):
        response = PostsChecks().create_new_post()
        (PostsChecks()
         .check_posts_response(response)
         .check_new_post_id(response))

    @allure.title("Метод: PUT /posts/[id]. Проверка обновления значений всех параметров в посте")
    def test_update_post(self):
        post_id = PostsChecks().get_existed_post_param("id")
        user_id = UsersChecks().get_existed_user_param("id")
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(1, 100)))
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().update_post(
            post_id=post_id,
            user_id=user_id,
            title=title,
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id,
            title=title,
            body=body
        )
         .check_post_id_after_update(response, post_id))

    @allure.title("Метод: PUT /posts/[id]. Проверка обновления части значений параметров в посте")
    def test_update_partial_post(self):
        # Проверка обновления только user_id
        post_id = PostsChecks().get_existed_post_param("id")
        user_id = UsersChecks().get_existed_user_param("id")
        response = PostsChecks().update_post(
            post_id=post_id,
            user_id=user_id
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id
        )
         .check_post_id_after_update(response, post_id))

        # Проверка обновления только title
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().update_post(
            post_id=post_id,
            title=title
        )
        (PostsChecks()
         .check_posts_response(
            response,
            title=title
        )
         .check_post_id_after_update(response, post_id))

        # Проверка обновления только body
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(1, 100)))
        response = PostsChecks().update_post(
            post_id=post_id,
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            body=body
        )
         .check_post_id_after_update(response, post_id))

    @allure.title("Метод: PUT /posts/[id]. Проверка обновления в посте user_id на несуществующий")
    def test_update_post_incorrect_user_id(self):
        post_id = PostsChecks().get_existed_post_param("id")
        user_id = UsersChecks().get_not_existed_user_id()
        response = PostsChecks().update_post(
            post_id=post_id,
            user_id=user_id
        )
        (PostsChecks()
         .check_posts_response(
            response,
            user_id=user_id
        )
         .check_post_id_after_update(response, post_id))

    @allure.title("Метод: PUT /posts/[id]. Проверка обновления поста с невалидным post_id")
    def test_update_post_incorrect_post_id(self):
        # Проверка id, которого нет в БД
        post_id = PostsChecks().get_not_existed_post_id()
        PostsChecks().update_post(
            post_id=post_id,
            status_code=requests.codes["server_error"]
        )
        # Проверка пустого id
        PostsChecks().update_post(
            post_id=EMPTY_STR,
            status_code=requests.codes["not_found"]
        )
        # Проверка невалидных значний id
        for value in INVALID_DATA_FOR_PARAMS:
            PostsChecks().update_post(
                post_id=value,
                status_code=requests.codes["server_error"]
            )

    @allure.title("Метод: PUT /posts/[id]. Проверка обновления поста с объемными title и body")
    def test_update_large_post(self):
        post_id = PostsChecks().get_existed_post_param("id")
        title = (PostsChecks()
                 .get_random_text_for_post(random.randint(4000, 4001)))
        body = (PostsChecks()
                .get_random_text_for_post(random.randint(4000, 4001)))
        response = PostsChecks().update_post(
            post_id=post_id,
            title=title,
            body=body
        )
        (PostsChecks()
         .check_posts_response(
            response,
            title=title,
            body=body
        )
         .check_post_id_after_update(response, post_id))

    @allure.title("Метод: DELETE /posts/[id]. Проверка ответа метода после удаления поста")
    def test_delete_post(self):
        post_id = PostsChecks().get_existed_post_param("id")
        response = PostsChecks().delete_post(post_id)
        PostsChecks().check_response_after_delete(response, EMPTY_DICT)

    @allure.title("Метод: DELETE /posts/[id]. Проверка удаления поста с несуществующим id")
    def test_delete_post_invalid_id(self):
        # Проверка id, которого нет в БД
        post_id = PostsChecks().get_not_existed_post_id()
        response = PostsChecks().delete_post(post_id)
        PostsChecks().check_response_after_delete(response, EMPTY_DICT)

        # Проверка пустого id
        response = PostsChecks().delete_post(
            EMPTY_STR,
            requests.codes["not_found"]
        )
        PostsChecks().check_response_after_delete(response, EMPTY_DICT)

        # Проверка невалидных значний id
        for value in INVALID_DATA_FOR_PARAMS:
            response = PostsChecks().delete_post(value)
            PostsChecks().check_response_after_delete(response, EMPTY_DICT)
