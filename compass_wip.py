import load_secrets_wip

def main():
    secret_name = "my_secret_name"
    load_secrets_wip.get_secret(secret_name)
    print("Secret retrieved successfully.")

