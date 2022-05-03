import requests

from unittest import TestCase


class TestApiGateway(TestCase):
    api_endpoint: str

    def setUp(self) -> None:
        self.api_endpoint = "http://127.0.0.1:3000"

    def test_sign_up_endpoint(self):
        response = requests.post(self.api_endpoint + "/signup")
        assert response.status_code == 201
