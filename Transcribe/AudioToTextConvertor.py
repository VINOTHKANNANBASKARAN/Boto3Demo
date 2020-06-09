from __future__ import print_function
import time
import boto3
import json
transcribe = boto3.client('transcribe')
job_name = "transcribefromboto3trial3"
job_uri = "https://transcibedemo.s3.ap-south-1.amazonaws.com/ttsMP3.com_VoiceText_2020-6-9_20_59_12.mp3"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US',
OutputBucketName='transcibedemo'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)

response = json.dumps(status)
print(response)