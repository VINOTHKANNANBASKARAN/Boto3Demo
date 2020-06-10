import json
import boto3
s3_client= boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file=event['Records'][0]['s3']['object']['key']
    print('bucket=',bucket)
    print('file=',json_file)
    result = s3_client.get_object(Bucket=bucket, Key=json_file)
    text = result["Body"].read().decode()
    result = json.loads(text)
    print(result)
    print(result['results']['transcripts'][0]['transcript'])
    return {
        'statusCode': 200,
        'transcript': result['results']['transcripts'][0]['transcript']
    }
