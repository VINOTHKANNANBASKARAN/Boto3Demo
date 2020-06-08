import boto3
ec2_client = boto3.client('ec2')

resp = ec2_client.describe_instances(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['running','terminated']
    }
    ]
)

#resp = ec2_client.describe_instances(Filters=[{
  #  'Name': 'tag:Env',
  #  'Values': ['Prod']
#}])

print(resp)
for instances in resp['Reservations']:
   # print(instances)
    for instance in instances['Instances']:
        print(str(instance['InstanceId']))
