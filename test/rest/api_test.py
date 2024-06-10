import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def do_request(self, url):
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_add_ok(self):
        url = f"{BASE_URL}/calc/add/2/2"
        self.do_request(url)

    def test_api_add_error(self):
        url = f"{BASE_URL}/calc/add/2/x"
        self.do_request(url)

    def test_api_subtract_ok(self):
        url = f"{BASE_URL}/calc/subtract/2/2"
        self.do_request(url)

    def test_api_subtract_error(self):
        url = f"{BASE_URL}/calc/subtract/2/x"
        self.do_request(url)

    def test_api_multiply_ok(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        self.do_request(url)

    def test_api_multiply_error(self):
        url = f"{BASE_URL}/calc/multiply/2/x"
        self.do_request(url)

    def test_api_divide_ok(self):
        url = f"{BASE_URL}/calc/divide/2/1"
        self.do_request(url)

    def test_api_divide_error(self):
        url = f"{BASE_URL}/calc/divide/2/x"
        self.do_request(url)

    def test_api_divide_by_zero_error(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        self.do_request(url)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/4/2"
        self.do_request(url)

    def test_api_power_error(self):
        url = f"{BASE_URL}/calc/power/4/x"
        self.do_request(url)

    def test_api_square_ok(self):
        url = f"{BASE_URL}/calc/square/64"
        self.do_request(url)

    def test_api_square_error(self):
        url = f"{BASE_URL}/calc/square/x"
        self.do_request(url)

    def test_api_square_negative_error(self):
        url = f"{BASE_URL}/calc/square/-64"
        self.do_request(url)

    def test_api_log10_ok(self):
        url = f"{BASE_URL}/calc/log10/10"
        self.do_request(url)

    def test_api_log10_error(self):
        url = f"{BASE_URL}/calc/log10/x"
        self.do_request(url)

    def test_api_log10_negative_error(self):
        url = f"{BASE_URL}/calc/log10/-10"
        self.do_request(url)
