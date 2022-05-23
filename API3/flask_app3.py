import boto3
from flask import Flask 

app = Flask(__name__)
dynamodb =boto3.resource('dynamodb')
client = boto3.client('iam')

@app.route('/showdetails')
def show_single_details_from_dynamodb():
    
    

    response = client.get_user(
        UserName='user1'
    )
    return response