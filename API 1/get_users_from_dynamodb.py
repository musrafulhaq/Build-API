import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('table1')
# client = boto3.client('dynamodb')

response = table.scan(

)
# print(response['Items'])

for item in response['Items']:
    print(item['users'])