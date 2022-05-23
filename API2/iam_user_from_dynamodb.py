import boto3
import json

dynamobd =boto3.resource('dynamodb')
iamUserInDynamodb = []

table=dynamobd.Table('table1')
response=table.scan()
for item in response['Items']:
    print(item['users'])
    iamUserInDynamodb.append(item['users'])

print(json.dumps({"users": iamUserInDynamodb}))

