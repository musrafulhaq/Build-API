import boto3
from flask import Flask
app = Flask(__name__)
dynamodb = boto3.client('dynamodb', region_name='ap-south-1')

@app.route('/createuser')

def create_user():
    client = boto3.client('iam')

    response = client.create_user(
        UserName='IAMTestUser'
    )

    return response