import boto3

ec2_client=boto3.client("ec2")
resp = ec2_client.stop_instances(
    InstanceIds=[
        'i-0aa9c7b41f051cebb'
    ]
)

print(resp)
try:
    for instance in resp['StoppingInstances']:
        print("Instance is "+str(instance['InstanceId']))
        print("PreviousState" +str(instance['PreviousState']))
        print("Current State" +str(instance['CurrentState']))

except Exception as err:
    print(err)
