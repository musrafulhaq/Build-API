import boto3
import json
from flask import Flask, jsonify


app = Flask(__name__)

dynamodb =boto3.resource('dynamodb')
iamUserInDynamodb = []

@app.route('/getuser')
def get_data_from_dynamodb():
    table=dynamodb.Table('table1')
    response=table.scan()
    for item in response['Items']:
        print(item['users'])
        iamUserInDynamodb.append(item['users'])

    print(json.dumps({"users": iamUserInDynamodb}))
    return jsonify({"users_in_db": iamUserInDynamodb})

