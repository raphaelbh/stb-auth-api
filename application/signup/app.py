import os
import sys
import json
import boto3


def lambda_handler(event, context):

    user = json.loads(event['body'])
    try:
        _sign_up(user)
        return {
            "statusCode": 201
        }
    except Exception:
        e = sys.exc_info()[1]
        body = json.dumps({
            "message": "Sign up error",
            "error": e.args[0]
        })
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": body
        }


def _sign_up(user):

    AWS_REGION = os.environ.get("AWS_REGION")
    USER_POOL_CLIENT_ID = os.environ.get("USER_POOL_CLIENT_ID")

    cognito_idp = boto3.client('cognito-idp', region_name=AWS_REGION)
    
    cognito_idp.sign_up(
        ClientId=USER_POOL_CLIENT_ID,
        Username=user['username'],
        Password=user['password'],
        UserAttributes=user['attributes']
    )
