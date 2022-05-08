import os
import sys
import json
import boto3


def lambda_handler(event, context):
    try:
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
