from dotenv import load_dotenv
import requests
import os 

load_dotenv()


def upload_to_pinata(file_path, jwt_token):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {'Authorization': f'Bearer {jwt_token}'}

    with open(file_path, 'rb') as file:
        response = requests.post(url, files = {'file': file }, headers=headers)
        return response.json()
    
PINATA_JWT_TOKEN = os.getenv('PINATA_JWT_TOKEN')

FILE_PATH = 'example.txt'

print(upload_to_pinata(FILE_PATH, PINATA_JWT_TOKEN))


