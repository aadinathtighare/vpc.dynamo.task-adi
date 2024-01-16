import boto3
 
def lambda_handler(event, context):
    # Define the CIDR range for the new VPC
    vpc_cidr = '10.0.0.0/16'
 
    # Create an EC2 client
    ec2 = boto3.client('ec2')
 
    try:
        # Create a new VPC
        response = ec2.create_vpc(CidrBlock=vpc_cidr)
 
        # Get the VPC ID from the response
        vpc_id = response['Vpc']['VpcId']
        print(f"VPC created successfully with ID: {vpc_id}")
 
        return {
            'statusCode': 200,
            'body': f'VPC created successfully with ID: {vpc_id}'
        }
    except Exception as e:
        print(f"Error creating VPC: {e}")
 
        return {
            'statusCode': 500,
            'body': f'Error creating VPC: {e}'
        }
