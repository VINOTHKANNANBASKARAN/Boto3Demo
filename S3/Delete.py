import boto3

client = boto3.client('s3')

response = client.delete_objects(
    Bucket='s3createbyboto3',
    Delete={
        'Objects': [
            {
                'Key': 'ironman'
            },{
                'Key': 'creates'
            },{
                'Key': 'scandynamodb'
            }
        ]})
print(response)