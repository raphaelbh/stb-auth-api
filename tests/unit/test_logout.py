import unittest

from unittest.mock import patch
from application.logout import app


class LogoutTestCase(unittest.TestCase):

    @patch('boto3.client')
    def test_lambda_handler_success(self, mock_boto_client):

        apigw_event = {
            "resource": "/users/logout",
            "httpMethod": "POST",
            "headers": {
                "Access-Token": "eyJraWQiOiJJeW..."
            }
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 204

    @patch('boto3.client')
    def test_lambda_handler_error(self, mock_boto_client):

        mock_boto_client.side_effect = Exception('Error')

        apigw_event = {
            "resource": "/users/logout",
            "httpMethod": "POST",
            "headers": {
                "Access-Token": "eyJraWQiOiJJeW..."
            }
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 500


if __name__ == '__main__':
    unittest.main()
