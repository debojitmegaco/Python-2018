from boto3 import Session
import re
import boto3
import logging

logging.basicConfig()
LOGGER = logging.getLogger()


user_name = ""
credentials_path = ""


with open(credentials_path, 'r') as file:
    file_data = file.read()
    environment = re.findall('\[.*?\]', file_data)
    for x in environment:
        profile_name = x[1:-1]
        print(f'Running on {profile_name}')
        session = Session(profile_name=profile_name)
        try:
            session = Session()
            credentials = session.get_credentials()
            current_credentials = credentials.get_frozen_credentials()

            client = boto3.client('iam')
            response = client.response = client.create_access_key(
                UserName=user_name
            )
            replaced_data = file_data.replace(current_credentials.access_key, response['AccessKey']['AccessKeyId'])
            replaced_data = replaced_data.replace(current_credentials.secret_key, response['AccessKey']['SecretAccessKey'])
            with open(f"{credentials_path}_tmp", 'w') as backup_file:
                backup_file.write(replaced_data)
        except Exception as e:
            LOGGER.error(e)
