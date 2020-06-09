import boto3

client = boto3.client('s3')
response = client.list_objects(
    Bucket='s3createbyboto3'

)

print(response)