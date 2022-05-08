import json
import unittest

from unittest.mock import patch
from application.login import app


class LoginTestCase(unittest.TestCase):

    @patch('boto3.client')
    def test_lambda_handler_success(self, mock_boto_client):

        mock_boto_client.return_value = mock_boto_client
        mock_boto_client.initiate_auth.return_value = {
            "AuthenticationResult": {
                "AccessToken": "AccessToken",
                "RefreshToken": "RefreshToken",
                "IdToken": "IdToken",
                "ExpiresIn": 3600
            }
        }

        body = json.dumps({
            "username": "raphaeldias.ti@gmail.com",
            "password": "Mudar@123"
        })
        apigw_event = {
            "body": body,
            "resource": "/users/login",
            "httpMethod": "POST"
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 200

    @patch('boto3.client')
    def test_lambda_handler_error(self, mock_boto_client):

        mock_boto_client.side_effect = Exception('Error')

        body = json.dumps({
            "username": "raphaeldias.ti@gmail.com",
            "password": "Mudar@123"
        })
        apigw_event = {
            "body": body,
            "resource": "/users/login",
            "httpMethod": "POST"
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 500


if __name__ == '__main__':
    unittest.main()
