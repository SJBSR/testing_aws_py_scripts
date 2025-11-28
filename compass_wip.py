import load_secrets_wip

def main():
    secret_name = "AWS_SECRET_KEY_ID"
    load_secrets_wip.get_secret(secret_name)
    print("Secret retrieved successfully.")
    secret_key = "AWS_SECRET_KEY"
    load_secrets_wip.get_secret(secret_key)

