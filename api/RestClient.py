import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType

from data.tests_constants import ALLURE_REQUEST, TXT, ALLURE_RESPONSE, EMPTY_DICT

logger = logging.getLogger(__name__)


class RestClient:
    def __init__(self):
        self.host = "https://jsonplaceholder.typicode.com"

    @allure.step("Валидация кода ответа")
    def validate_response_code(
            self,
            response: requests.Response,
            ok_status=requests.codes['ok']
    ):
        """
        Метод для валидации кода ответа
        :param response: тело ответа
        :param ok_status: ожидаемый код ответа
        """
        if response.status_code != ok_status:
            raise ValueError(
                f"Validation failed for {response.url}, "
                f"status code: {response.status_code} "
                f"with message: {response.text}"
            )
        else:
            logger.info(
                f"Validation successful for {response.url}"
            )
        return response

    vr = validate_response_code

    def post(
            self, url, body=EMPTY_DICT, params=None,
            headers=None, status_code=requests.codes['ok']
             ):
        """
        Метод для создания post запроса с документированием тела запроса и ответа в allure
        :param url: url запроса
        :param body: тело запроса
        :param params: параметры запроса
        :param headers: заголовки запроса
        :param status_code: ожидаемый код ответа
        """
        allure.attach(
            name=ALLURE_REQUEST,
            body=json.dumps(body, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        response = self.vr(
            requests.post(
                self.host + url,
                json=body,
                params=params,
                headers=headers
            ),
            ok_status=status_code
        ).text
        allure.attach(
            name=ALLURE_RESPONSE,
            body=json.dumps(response, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        return json.loads(response)

    def put(
            self, url, body=EMPTY_DICT, params=None,
            headers=None, status_code=requests.codes['ok']
    ):
        """
        Метод для создания put запроса с документированием тела запроса и ответа в allure
        :param url: url запроса
        :param body: тело запроса
        :param params: параметры запроса
        :param headers: заголовки запроса
        :param status_code: ожидаемый код ответа
        """
        allure.attach(
            name=ALLURE_REQUEST,
            body=json.dumps(body, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        response = self.vr(
            requests.put(
                self.host + url,
                json=body,
                params=params,
                headers=headers
            ),
            ok_status=status_code
        ).text
        allure.attach(
            name=ALLURE_RESPONSE,
            body=json.dumps(response, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        if status_code == requests.codes['ok']:
            response_body = json.loads(response)
        else:
            response_body = response
        return response_body

    def delete(self, url, status_code=requests.codes['ok']):
        """
        Метод для создания delete запроса с документированием тела ответа в allure
        :param url: url запроса
        :param status_code: ожидаемый код ответа
        """
        response = self.vr(
            requests.delete(
                self.host + url
            ),
            ok_status=status_code
        ).text
        allure.attach(
            name=ALLURE_RESPONSE,
            body=json.dumps(response, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        return json.loads(response)

    def get(self, url, params=None, status_code=requests.codes['ok']):
        """
        Метод для создания get запроса с документированием тела ответа в allure
        :param url: url запроса
        :param params: параметры запроса
        :param status_code: ожидаемый код ответа
        """
        response = self.vr(
            requests.get(
                self.host + url,
                params=params
            ),
            ok_status=status_code
        ).text
        allure.attach(
            name=ALLURE_RESPONSE,
            body=json.dumps(response, indent=4),
            attachment_type=AttachmentType.JSON,
            extension=TXT
        )
        return json.loads(response)

    @allure.step("Валидация тела ответа")
    def validate_response_body(self, schema, response):
        """
        :param schema: схема, используемая для валидации ответа
        :param response: тело ответа
        """
        errors = schema.validate(response)
        if len(errors) > 0:
            raise ValueError(
                f"Validation failed, incorrect attributes: {errors} "
            )

    @allure.step("Создание запроса")
    def create_request(self, schema, request):
        """
        :param schema: схема, используемая для создания запроса
        :param request: данные запроса
        :return:
        """
        return schema.dump(request)
