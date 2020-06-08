import boto3

ec2_client= boto3.client("ec2")
resp = ec2_client.run_instances(
                        ImageId='ami-0447a12f28fddb066',
                         InstanceType='t2.micro',
                         MaxCount=1,
                         MinCount=1,
                         )
print("response ", resp)

for instance in resp['Instances']:
    print(instance['InstanceId'])