import boto3

client = boto3.client('dynamodb')
response = client.put_item(
    TableName='Students',
    Item={
        'id': {'S':'127'},
        'name': {'S':'Rohit'},
        'age': {'N':'35'},
        'isMale': {'BOOL':True},
        'course':{'S':'HitMan'}
    })
print(response)
