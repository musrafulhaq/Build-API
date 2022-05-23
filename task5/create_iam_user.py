
# import boto3

# dynamobd =boto3.resource('dynamodb')

# table=dynamobd.Table('table1')

# response = table.create_table(
#     AttributeDefinitions=[
#         {
#             'users': 'user2',
#             'AttributeType': 'S'
#         },
#     ],
# )

# response = table.get_user()
# for item in response['Items']:
#     print(item['users'])

import boto3

client = boto3.client('iam')

response = client.create_user(
    UserName='IAMTestUser'
)

print(response)