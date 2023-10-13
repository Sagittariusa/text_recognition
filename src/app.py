import json

from src.recognizer import read_image


def lambda_handler(event, context):
    if body := event.get('body'):
        res = read_image(body)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({"text": res})
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"error": "No body provided"})
    }
