import urllib

import boto3
import json
transcribe = boto3.client('transcribe')

response = transcribe.get_transcription_job(
    TranscriptionJobName='transcribefromboto3trial3'
)
status = response
if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    response = urllib.urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
    data = json.loads(response.read())
    text = data['results']['transcripts'][0]['transcript']
    print(text)

print(response)
print(response['TranscriptionJob']['Transcript'])