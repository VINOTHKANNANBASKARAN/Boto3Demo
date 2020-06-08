import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')
response = table.update_item(
    Key={
        'id':'124'
    },
    AttributeUpdates={
         'course': {
            'Value': 'Run Machine',
            'Action': 'PUT'
        }
    }
)
print(response)