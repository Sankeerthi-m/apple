xmport json
<<<<<<< HEAD
import boto223
=======
import boto2
>>>>>>> 42819ad510256f84136ad18446ec70f163eea82a


def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
    ImageId='ami-0614680123427b75e',
    InstanceType='t2.micro',
    KeyName='mykeymumbai',
    MaxCount=2,
    MinCount=2
)

