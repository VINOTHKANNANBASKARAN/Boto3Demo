import boto3

client = boto3.client('s3')
file = open('C:\\Data\\Codebase\\python\\aws-boto-demo\\DynamoDB\\ScanDDb.py').read()
response = client.put_object(
    ACL='public-read',
    Body=file,
    Bucket='s3createbyboto3',
    Key='scandynamodb'
)

print(response)