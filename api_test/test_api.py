import pytest
import os
import requests
from hamcrest import *
import allure


@pytest.mark.api
@allure.feature("Датчик температуры")
class TestTemperatureSensor:
    """
    API
    """

    def setup_method(self):
        host = os.environ.get("testHost", "localhost:8888")
        command = "temperature_check"
        self.url = f"http://{host}/{command}"

    @pytest.mark.parametrize("temperature, status, condition",
                             [("-274K", 400, '"error": "invalid temperature'),
                              ("-273K", 200, "ice"),
                              ("-272K", 200, "ice"),
                              ("-1K", 200, "ice"),
                              ("0K", 200, "ice"),
                              ("1K", 200, "liquid"),
                              ("99K", 200, "liquid"),
                              ("100K", 200, "steam"),
                              ("101K", 200, "steam"),
                              ("1000000K", 200, "steam")
                              ])
    @allure.title("Тест шкалы Цельсия")
    @allure.description("Тест проверяет взаимосвязь состояния воды и шкалы Цельсия")
    def test_celsius(self, temperature, status, condition):
        """
        Celsius scale
        """

        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status))
        response_text = response.text.strip().lower()
        assert_that(response_text, contains_string(condition))

    @pytest.mark.parametrize("temperature, status, condition",
                             [("373C", 200, "steam"),
                              ("374C", 200, "steam"),
                              ("100000000C", 200, "steam"),
                              ("274C", 200, "liquid"),
                              ("372C", 200, "liquid"),
                              ("-1C", 400, '"error": "invalid temperature'),
                              ("0C", 200, "ice"),
                              ("1C", 200, "ice"),
                              ("272C", 200, "ice"),
                              ("273C", 200, "ice")
                              ])
    @allure.title("Тест шкалы Кельвина")
    @allure.description("Тест проверяет взаимосвязь состояния воды и шкалы Кельвина")
    def test_kelvin(self, temperature, status, condition):
        """
        Kelvin scale
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, contains_string(condition))

    @pytest.mark.parametrize("temperature, status, condition",
                             [("212F", 200, "steam"),
                              ("214F", 200, "steam"),
                              ("180000032F", 200, "steam"),
                              ("34F", 200, "liquid"),
                              ("210F", 200, "liquid"),
                              ("-459F", 200, "ice"),
                              ("-461F", 400, '"error": "invalid temperature'),
                              ("-458F", 200, "ice"),
                              ("30F", 200, "ice"),
                              ("32F", 200, "ice")
                              ])
    @allure.title("Тест шкалы Фаренгейта")
    @allure.description("Тест проверяет взаимосвязь состояния воды и шкалы Фаренгейта")
    def test_fahrenheit(self, temperature, status, condition):
        """
        Fahrenheit scale
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, contains_string(condition))

    @pytest.mark.parametrize("temperature, status, condition",
                             [('<script>alert("XSS1")</script>', 400, '"error": "invalid temperature'),
                              ("' OR 1=1#", 400, '"error": "invalid temperature'),
                              ("123456789011121314151617181920212223242526272829303132333K", 400,
                               '"error": "invalid temperature'),
                              ("3,234,56K", 400, '"error": "invalid temperature'),
                              ("3,1230K", 400, '"error": "invalid temperature'),
                              ("057K", 400, '"error": "invalid temperature'),
                              ("4,7K", 400, '"error": "invalid temperature'),
                              ("4.7K", 400, '"error": "invalid temperature'),
                              ("√8K", 400, '"error": "invalid temperature'),
                              ("23/24K", 400, '"error": "invalid temperature'),
                              ("%", 400, '"error": "invalid temperature'),
                              ("♣", 400, '"error": "invalid temperature'),
                              ("☺", 400, '"error": "invalid temperature'),
                              ("+30K", 400, '"error": "invalid temperature'),
                              ("17K ", 400, '"error": "invalid temperature'),
                              (" 11K", 400, '"error": "invalid temperature'),
                              ("[1,2,3]K", 400, '"error": "invalid temperature'),
                              ("14 K", 400, '"error": "invalid temperature'),
                              (" ", 400, '"error": "invalid temperature'),
                              ("C23", 400, '"error": "invalid temperature'),
                              ("7R", 400, '"error": "invalid temperature'),
                              ("K", 400, '"error": "invalid temperature'),
                              ("10c", 400, '"error": "invalid temperature'),
                              ("%20", 400, '"error": "invalid temperature'),
                              ("-1", 400, '"error": "invalid temperature'),
                              ("0", 400, '"error": "invalid temperature'),
                              ("1", 400, '"error": "invalid temperature'),
                              ("", 400, '"error": "invalid temperature'),
                              ])
    @allure.title("Негативные сценарии")
    @allure.description("Тест проверяет негативные сценарии")
    def test_equivalence_classes(self, temperature, status, condition):
        """
        Negative
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status))
        response_text = response.text.strip().lower()
        assert_that(response_text, contains_string(condition))

    @pytest.mark.parametrize("temperature, status, condition", [("1K", 400, '{"error": "invalid json format"}')])
    @allure.title("Смена метода запроса")
    @allure.description("Тест проверяет смену метода запроса")
    def test_post_method(self, temperature, status, condition):
        """
        POST method
        """
        response = requests.post(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status))
        response_text = response.text.strip().lower()
        assert_that(response_text, contains_string(condition))

    @pytest.mark.parametrize("adfgafdv, status, condition", [("17K", 400, '{"error": "Bad Request"}')])
    @allure.title("Тест ошибки в параметре")
    @allure.description("Тест проверяет наличие ошибки в параметре температуры")
    def test_parameter_mistake(self, adfgafdv, status, condition):
        """
        Wrong parameter
        """
        response = requests.get(self.url, params={"adfgafdv": "17K"})
        assert_that(response.status_code, equal_to(status))
        assert_that(response.text, contains_string(condition))
