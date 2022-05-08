import os
import sys
import json
import boto3


def lambda_handler(event, context):

    user = json.loads(event['body'])
    try:
        auth_result = _initiate_auth(user)
        body = json.dumps({
            "access_token": auth_result["AuthenticationResult"]["AccessToken"],
            "refresh_token": auth_result["AuthenticationResult"]["RefreshToken"],
            "id_token": auth_result["AuthenticationResult"]["IdToken"],
            "expires_in": auth_result["AuthenticationResult"]["ExpiresIn"]
        })

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": body
        }
    except Exception:
        e = sys.exc_info()[1]
        body = json.dumps({
            "error": e.args[0]
        })
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": body
        }


def _initiate_auth(user):

    AWS_REGION = os.environ.get("AWS_REGION")
    USER_POOL_CLIENT_ID = os.environ.get("USER_POOL_CLIENT_ID")

    cognito_idp = boto3.client('cognito-idp', region_name=AWS_REGION)

    return cognito_idp.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': user['username'],
            'PASSWORD': user['password']
        },
        ClientId=USER_POOL_CLIENT_ID
    )
