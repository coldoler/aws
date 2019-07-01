import json
import boto3


def hello(event, context):

    client = boto3.client('lambda')
    print(event)
    response = client.list_functions()

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
