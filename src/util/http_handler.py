"""Send GET request to AWS to retrieve data"""
import requests
from requests.exceptions import HTTPError

endpoint = """https://4tjfjgbpw5.execute-api.us-east-2.amazonaws.com/default/upload-DB-python"""
api_key = "CTLJlMqQpt16yPsEEDzEM7dJPLSkilsl19pEB15f"


def get(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
