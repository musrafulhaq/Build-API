import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('table1')

client = boto3.client('dynamodb')

response = table.scan(

)
for item in response['Items']:
    print(item)

    res = client.delete_item(
        TableName='table1',
        Key={
            'users': {'S': item['users']}
        }
    )
    print(res, end='\n\n')