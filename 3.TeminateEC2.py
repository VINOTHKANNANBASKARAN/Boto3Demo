import boto3

ec2_client = boto3.client('ec2')

resp = ec2_client.terminate_instances(
    InstanceIds=[
        'i-0aa9c7b41f051cebb'
    ]
)


print(resp)

for values in resp['TerminatingInstances']:
    print('Instance ID '+ str(values['InstanceId']))
    print('Current state '+ str(values['CurrentState']))
    print('Previous Statae' + str(values['PreviousState']))