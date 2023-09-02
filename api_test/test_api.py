import pytest
import os
import requests
from hamcrest import *


class TestTemperatureChecker:
    """
    API
    """

    def setup_method(self):
        host = os.environ.get("testHost", "localhost:8888")
        command = "temperature_check"
        self.url = f"http://{host}/{command}"

    @pytest.mark.parametrize("temperature, status, condition",
                             [("-274K", 400, "unknown"), ("-273K", 200, "ice"), ("-272K", 200, "ice"),
                              ("-1K", 200, "ice"), ("0K", 200, "ice")])
    def test_id1(self, temperature, status, condition):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("1K", 200, "liquid"), ("99K", 200, "liquid")])
    def test_id2(self, temperature, status, condition):
        """
        Boarder values Celsius liquid
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("100K", 200, "steam"), ("101K", 200, "steam"), ("1000000K", 200, "steam")])
    def test_id3(self, temperature, status, condition):
        """
        Boarder values Celsius steam
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("-1C", 400, "unknown"), ("0C", 200, "ice"), ("1C", 200, "ice"),
                              ("272C", 200, "ice"), ("273", 200, "ice")])
    def test_id4(self, temperature, status, condition):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("274C", 200, "liquid"), ("372C", 200, "liquid")])
    def test_id5(self, temperature, status, condition):
        """
        Boarder values Kelvin liquid
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("373C", 200, "steam"), ("374C", 200, "steam"), ("1000000C", 200, "steam")])
    def test_id6(self, temperature, status, condition):
        """
        Boarder values Kelvin steam
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("-461,2F", 400, "unknown"), ("-459,4F", 200, "ice"), ("-457,6F", 200, "ice"),
                              ("30,2F", 200, "ice"), ("32F", 200, "ice")])
    def test_id7(self, temperature, status, condition):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("33,8F", 200, "liquid"), ("210,2FC", 200, "liquid")])
    def test_id8(self, temperature, status, condition):
        """
        Boarder values Fahrenheit liquid
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("212F", 200, "steam"), ("213,8F", 200, "steam"), ("1800032F", 200, "steam")])
    def test_id9(self, temperature, status, condition):
        """
        Boarder values Fahrenheit steam
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    def test_equivalence_classes_id10(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": ""})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id11(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "%20"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    @pytest.mark.parametrize("temperature, status, condition",
                             [("-1", 400, "unknown"), ("0", 400, "unknown"), ("1", 400, "unknown")])
    def test_id12(self, temperature, status, condition):
        """
        Boarder values Fahrenheit steam
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    def test_equivalence_classes_id13(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "10c"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id14(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id15(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "7R"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id16(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "C23"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id17(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": " "})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id18(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "14 K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id19(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "1&[1,b,$]"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id20(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": " 11K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id21(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "17K "})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id22(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "+30K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    @pytest.mark.parametrize("temperature, status, condition",
                             [("%", 400, "unknown"), ("♣", 400, "unknown"), ("☺", 400, "unknown")])
    def test_id23(self, temperature, status, condition):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    @pytest.mark.parametrize("temperature, status, condition",
                             [("4,7K", 400, "unknown"), ("4.7K", 400, "unknown"), ("√8K", 400, "unknown"),
                              ("23/24K", 400, "unknown")])
    def test_id24(self, temperature, status, condition):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    def test_equivalence_classes_id25(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "057K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id26(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "3,1230K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id27(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "3,234,56K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_parameter_mistake_id28(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperture": "17K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    @pytest.mark.parametrize("temperature, status, condition",
                             [("12345678901112131415161718192021222324252627282930313233K", 400, "unknown"),
                              ("123456789011121314151617181920212223242526272829303132333K", 400, "unknown"),
                              ("1234567890111213141516171819202122232425262728293031323334K", 400, "unknown")])
    def test_id29(self, temperature, status, condition):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": temperature})
        assert_that(response.status_code, equal_to(status)),
        response_text = response.text.strip().lower()
        assert_that(response_text, equal_to(condition)),

        return response

    def test_id30(self):
        """
        Equivalence classes
        """
        response = requests.post(self.url, params={"temperature": "1K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_id31(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "' OR 1=1#"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_id32(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "<script>alert("XSS1")</script>"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))
