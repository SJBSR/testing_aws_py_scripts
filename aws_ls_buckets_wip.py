# List S3 buckets in AWS account
import boto3

s3 = boto3.client("s3")

def client():
    return boto3.client("s3")

def list_buckets():
    return client().list_buckets()

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])