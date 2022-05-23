import boto3

client = boto3.client('iam')

response = client.list_users(
    PathPrefix='/'
)

# print("List of users: {}".format(response['Users']), end='\n\n')

# print("Ist user: {}".format(response['Users'][0]))
# print("2nd user: {}".format(response['Users'][1]))
# print("3rd user: {}".format(response['Users'][2]))


# print("Ist user's name: {}".format(response['Users'][0]['UserName']), end='\n\n')


for user in response['Users']:
    print(user['UserName'], end='\n\n')

