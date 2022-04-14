def lambda_handler(event, context):
    return {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        }
    }