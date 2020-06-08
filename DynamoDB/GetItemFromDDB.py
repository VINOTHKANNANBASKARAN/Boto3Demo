import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')
response = table.get_item(
    Key={
        'id':'123'
    },
    #returns only items specified here
    AttributesToGet=[
        'id','name','age'
    ]
)

print(response['Item'])