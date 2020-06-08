import boto3
dynamodb =boto3.resource('dynamodb')
table = dynamodb.Table('Students')
response = table.scan()

for item in response['Items']:

        print(item)


