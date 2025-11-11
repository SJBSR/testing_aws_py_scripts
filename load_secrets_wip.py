import boto3

def get_secret(secret_name):
    secret_name = secret_name
    region_name = "us-east-1"

    #create secrets manager client
    session = boto3
    client = session.client(
        service_name = 'secretsmanager',
        region_name = region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    secret = get_secret_value_response['SecretString']
    print(secret)