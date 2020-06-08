import boto3

ec2_resource=boto3.resource('ec2')
for instance  in ec2_resource.instances.filter(Filters=
    [
        {
            'Name':'availability-zone',
            "Values": ['ap-south-1a']
        }
    ]
):
    print('Instance id {} and Instance Type {}'.format(instance.instance_id, instance.instance_type))