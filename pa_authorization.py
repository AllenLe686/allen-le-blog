import os
import requests
from dotenv import load_dotenv

load_dotenv()

username = os.environ["PA_USERNAME"]
token = os.environ["PA_API_TOKEN"]

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))