from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feeds']
SECRETS_FILE = 'data-rookery-309413-5578c70a0a89.json'
SPREADSHEET = 'Ethical Benefits and Implications (Responses)'

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials =  ServiceAccountCredentials(json_key['client_email'], json_key['private_key'], SCOPE)

#print(type(json_key['private_key']))
gc = gspread.authorize(credentials)
workbook = gc.open(SPREADSHEET)
# Get the first sheet
sheet = workbook.sheet1
data = pd.DataFrame(sheet.get_all_records())

column_names = {'Timestamp': 'timestamp',
                'What future technology is featured in your synopsis?': 'future-tech',
                'What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?': 'ethical-issues',
                'What do you think might be a cautionary tale related to this technology?': 'cautionary'
                }
data.rename(columns=column_names, inplace=True)
data.timestamp = pd.to_datetime(data.timestamp)
print(data.head())
