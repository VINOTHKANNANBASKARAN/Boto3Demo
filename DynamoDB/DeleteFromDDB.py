import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')
response = table.delete_item(
    Key={
        'id':'125'
    }
)

print(response)