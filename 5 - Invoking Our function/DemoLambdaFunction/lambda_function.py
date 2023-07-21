import json

def lambda_handler(event, context):
    value = event['key1']
    print(value)