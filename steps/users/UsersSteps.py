import random

import allure

from api.UsersApi import UsersApi


class UsersSteps(UsersApi):

    @allure.step('Получить существующий {param} пользователя')
    def get_existed_user_param(self, param):
        users = self.get_users()
        params = [user.get(param) for user in users]
        random_value = random.choice(params)
        return random_value

    @allure.step("Получить не существующий id пользователя")
    def get_not_existed_user_id(self):
        users = self.get_users()
        id_users = [user.get("id") for user in users]
        user_id = id_users[-1] + 1
        return user_id

    @allure.step('Получить часть значения из параметра {param}')
    def get_part_param_value(self, param):
        value = self.get_existed_user_param(param)
        part_value = value[
                     random.randint(0, len(value) // 2):
                     random.randint(len(value) // 2 + 1, len(value))
                     ]
        return part_value
