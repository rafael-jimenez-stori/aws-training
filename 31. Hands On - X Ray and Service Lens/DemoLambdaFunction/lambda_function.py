import json
import sys
import boto3
from boto3.dynamodb.conditions import Key, attr

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

#Setup_SNS_Client
sns_client = boto3.client('sns')
table = dynamodb.Table('CustomerOrdersTable')


def lambda_handler(event, context):
    
    #Query DynamoDB
   items = query_dynamo("1")

   #Filter items
   filtered_items = filter_items(items)

   #Publish filtered items to SNS
   publish_to_sns(filtered_items)

def query_dynamo(customerId: str) -> list:
   response = table.query(KeyConditionExpression=key('CustomerId').eq('1'))
   return response['Items']

@xray_recorder.capture("filter_items")
def filter_items(items: list) -> list:
   result = []
   for item in items:
      if item["OrderState"] == "APPROVED":
         result.append(item["CustomerId"])
   return result
   

def publish_to_sns(items: list):
   #Raise Exception('Something went horriblhy wrong')
   sns_client.publish(TopicArn="arn:aws:sns:us-east-1:346538479049", Message=json.dump({'items': items}))