import gspread
import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials

# This is the mysqlcredentials.py file containing your credentials.
#import mysqlcredentials as mc
# https://betterprogramming.pub/automating-data-extractions-from-google-sheets-with-python-666a692d8ac2

# The required variables for gspread:
scope = ['https://spreadsheets.google.com/feeds', \
       'https://www.googleapis.com/auth/drive']

# The credentials created for the service account in your Google project
# is stored in a .json file after you click 'Create Key'
# I renamed this file to sheetstodb.json.
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

def GetSpreadsheetData(sheetName, worksheetIndex):
   sheet = client.open_by_url(sheetName).get_worksheet(worksheetIndex)
   return sheet.get_all_values()[1:]
