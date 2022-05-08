import json
import unittest

from unittest.mock import patch
from application.signup import app


class SignUpTestCase(unittest.TestCase):

    @patch('boto3.client')
    def test_lambda_handler_success(self, mock_boto_client):

        body = json.dumps({
            "username": "raphaeldias.ti@gmail.com",
            "password": "Mudar@123",
            "attributes": [{
                "Name": "name",
                "Value": "Raphael Oliveira"
            }, {
                "Name": "email",
                "Value": "raphaeldias.ti@gmail.com"
            }]
        })
        apigw_event = {
            "body": body,
            "resource": "/signup",
            "httpMethod": "POST"
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 201

    @patch('boto3.client')
    def test_lambda_handler_error(self, mock_boto_client):

        mock_boto_client.side_effect = Exception('Error')

        body = json.dumps({
            "username": "raphaeldias.ti@gmail.com",
            "password": "Mudar@123",
            "attributes": [{
                "Name": "name",
                "Value": "Raphael Oliveira"
            }, {
                "Name": "email",
                "Value": "raphaeldias.ti@gmail.com"
            }]
        })
        apigw_event = {
            "body": body,
            "resource": "/signup",
            "httpMethod": "POST"
        }

        response = app.lambda_handler(apigw_event, "")
        assert response["statusCode"] == 500


if __name__ == '__main__':
    unittest.main()
