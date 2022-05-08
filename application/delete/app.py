import os
import sys
import json
import boto3


def lambda_handler(event, context):
    try:
        access_token = event["headers"]["Access-Token"]
        _delete_user(access_token)
        return {
            "statusCode": 204
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


def _delete_user(access_token):

    AWS_REGION = os.environ.get("AWS_REGION")
    cognito_idp = boto3.client('cognito-idp', region_name=AWS_REGION)

    cognito_idp.delete_user(
        AccessToken=access_token
    )
