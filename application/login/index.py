import json


def lambda_handler(event, context):

    body = json.dumps({
        "access_token": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
        "token_type": "Bearer",
        "expires_in": 3600,
        "refresh_token": "IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk"
    })

    return {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": body
    }
