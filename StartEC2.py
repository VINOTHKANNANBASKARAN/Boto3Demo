import boto3

ec2_client = boto3.client("ec2")

resp = ec2_client.start_instances(InstanceIds=['i-05e8e80265278c870'])

print(resp)

for values in resp['StartingInstances']:
    print('Instance ID '+ str(values['InstanceId']))
    print('Current state '+ str(values['CurrentState']))
    print('Previous state '+ str(values['PreviousState']))