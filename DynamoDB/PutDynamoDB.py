import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')
table.put_item(
    Item={
        'id':'124',
        'name':'VK',
        'age':32,
        'isMale':True

    })