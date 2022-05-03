import json
import pytest

from application.signup import app


@pytest.fixture()
def apigw_event():
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
    return {
        "body": body,
        "resource": "/signup",
        "httpMethod": "POST"
    }


def test_lambda_handler_success(apigw_event):
    response = app.lambda_handler(apigw_event, "")
    assert response["statusCode"] == 201
