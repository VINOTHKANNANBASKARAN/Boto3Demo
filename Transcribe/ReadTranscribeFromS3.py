import boto3
import json
BUCKET = 'transcibedemo'
FILE_TO_READ = 'transcribefromboto3trial3.json'
s3 = boto3.resource('s3')

content_object = s3.Object(BUCKET, FILE_TO_READ)
file_content = content_object.get()['Body'].read().decode('utf-8')
json_content = json.loads(file_content)
print(json_content)
print(json_content['results']['transcripts'][0]['transcript'])

