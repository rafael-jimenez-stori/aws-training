import json

def lambda_handler(event, context):
   personId = event["queryStringParameters"]["personId"]

   print("The personId extracted from the GET request is " + str(personId))
   #Call Database with personID=5
   return {"firstName":"Daniel"} 
   # return{
   #    'statusCode':200,
   #    'body': json.dumps('Hello from lambda!')
   # }