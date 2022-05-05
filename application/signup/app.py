import os
import json


def lambda_handler(event, context):
    body = json.dumps({
        "REGION": os.environ.get("REGION"),
        "AWS_REGION": os.environ.get("AWS_REGION"),
        "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION"),
        "USER_POOL_ID": os.environ.get("USER_POOL_ID"),
        "USER_POOL_CLIENT_ID": os.environ.get("USER_POOL_CLIENT_ID")
    })

    return {
        "statusCode": 201,
        "body": body
    }

