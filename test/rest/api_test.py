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
        try:
            return urlopen(url, timeout=DEFAULT_TIMEOUT)
        except HTTPError as e:
            self.assertEqual(
                e.code, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_api_add_ok(self):
        url = f"{BASE_URL}/calc/add/2/2"
        self.do_request(url)

    def test_api_subtract_ok(self):
        url = f"{BASE_URL}/calc/subtract/2/2"
        self.do_request(url)