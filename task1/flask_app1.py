import boto3
from flask import Flask, jsonify


app = Flask(__name__)
client = boto3.client('iam')
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

def listIamUser():
    iamUsers = []
    response = client.list_users(
        PathPrefix='/')

    for user in response['Users']:
        iamUsers.append(user['UserName'])
    return iamUsers


@app.route('/addusers')
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
    return jsonify({"users": retrievedIamUsers})




