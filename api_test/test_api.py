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

    def test_boarder_values_id1_1(self):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": "-274K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_boarder_values_id1_2(self):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": "-273K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id1_3(self):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": "-272K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id1_4(self):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": "-1K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id1_5(self):
        """
        Boarder values Celsius ice
        """
        response = requests.get(self.url, params={"temperature": "0K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id2_1(self):
        """
        Boarder values Celsius liquid
        """
        response = requests.get(self.url, params={"temperature": "1K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id2_2(self):
        """
        Boarder values Celsius liquid
        """
        response = requests.get(self.url, params={"temperature": "99K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id3_1(self):
        """
        Boarder values Celsius steam
        """
        response = requests.get(self.url, params={"temperature": "100K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id3_2(self):
        """
        Boarder values Celsius steam
        """
        response = requests.get(self.url, params={"temperature": "101K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id3_3(self):
        """
        Boarder values Celsius steam
        """
        response = requests.get(self.url, params={"temperature": "1000000000K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id4_1(self):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": "-1C"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_boarder_values_id4_2(self):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": "0C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id4_3(self):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": "1C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id4_4(self):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": "272C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id4_5(self):
        """
        Boarder values Kelvin ice
        """
        response = requests.get(self.url, params={"temperature": "273C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id5_1(self):
        """
        Boarder values Kelvin liquid
        """
        response = requests.get(self.url, params={"temperature": "274C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id5_2(self):
        """
        Boarder values Kelvin liquid
        """
        response = requests.get(self.url, params={"temperature": "372C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id6_1(self):
        """
        Boarder values Kelvin steam
        """
        response = requests.get(self.url, params={"temperature": "373C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id6_2(self):
        """
        Boarder values Kelvin steam
        """
        response = requests.get(self.url, params={"temperature": "374C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id6_3(self):
        """
        Boarder values Kelvin steam
        """
        response = requests.get(self.url, params={"temperature": "1000000000C"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id7_1(self):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": "-461,2"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_boarder_values_id7_2(self):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": "-459,4F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id7_3(self):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": "-457,6F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id7_4(self):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": "30,2F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id7_5(self):
        """
        Boarder values Fahrenheit ice
        """
        response = requests.get(self.url, params={"temperature": "32F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("ice"))

    def test_boarder_values_id8_1(self):
        """
        Boarder values Fahrenheit liquid
        """
        response = requests.get(self.url, params={"temperature": "33,8F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id8_2(self):
        """
        Boarder values Fahrenheit liquid
        """
        response = requests.get(self.url, params={"temperature": "210,2F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_boarder_values_id9_1(self):
        """
        Boarder values Fahrenheit steam
        """
        response = requests.get(self.url, params={"temperature": "212F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id9_2(self):
        """
        Boarder values Fahrenheit steam
        """
        response = requests.get(self.url, params={"temperature": "213,8F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

    def test_boarder_values_id9_3(self):
        """
        Boarder values Fahrenheit steam
        """
        response = requests.get(self.url, params={"temperature": "1800032F"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("steam"))

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

    def test_equivalence_classes_id12_1(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "-1"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id12_2(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "0"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id12_3(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "1"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

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

    def test_equivalence_classes_id23_1(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "%"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id23_2(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "♣"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id23_3(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "☺"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id24_1(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "4,7K"})
        assert_that(response.status_code, equal_to(200))
        assert_that(response.text, equal_to("liquid"))

    def test_equivalence_classes_id24_2(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "4.7K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id24_3(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "√8K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id24_4(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "23/24K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

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

    def test_equivalence_classes_id29_1(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "12345678901112131415161718192021222324252627282930313233K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id29_2(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "123456789011121314151617181920212223242526272829303132333K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_equivalence_classes_id29_3(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "1234567890111213141516171819202122232425262728293031323334K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_method_post_id30(self):
        """
        Equivalence classes
        """
        response = requests.post(self.url, params={"temperature": "1K"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_sql_injection_id31(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "' OR 1=1#"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))

    def test_html_injection_id32(self):
        """
        Equivalence classes
        """
        response = requests.get(self.url, params={"temperature": "<script>alert("XSS1")</script>"})
        assert_that(response.status_code, equal_to(400))
        assert_that(response.text, equal_to("unknown"))






