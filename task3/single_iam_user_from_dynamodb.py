import boto3

client = boto3.client('iam')

response = client.get_user(
    UserName='user1'
)

print(response)