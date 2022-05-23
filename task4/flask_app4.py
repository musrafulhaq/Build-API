import boto3
import json
from flask import Flask, jsonify
app = Flask(__name__)

# dynamodb =boto3.resource('dynamodb')
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

iamUserInDynamodb = []

client = boto3.client('iam')

@app.route('/appenduser')

# dynamodb = boto3.resource('dynamodb', region='ap-south-1')
# table = dynamodb.Table('table1')

def listIamUser():
    iamUsers = []
    response = client.list_users(
        PathPrefix='/')

    for user in response['Users']:
        print(user['UserName'], end='\n\n')
        iamUsers.append(user['UserName'])
    return iamUsers

def putUserIntoDynamodb():
    retrievedIamUsers = listIamUser()
    for iamUser in retrievedIamUsers:
        response = dynamodb.put_item(
            TableName='table1',
            Item={
                'users': {
                    'S': iamUser
                }
            }
        )
        print(response)
    return 'Users have been added succesfully'

print(putUserIntoDynamodb())

