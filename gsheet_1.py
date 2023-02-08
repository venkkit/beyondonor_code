# %%
from __future__ import print_function
import os.path
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pandas import *
import csv
import sys
import pandas as pd

# check the folder exist or not
import os
if not os.path.exists('output1'):
   os.makedirs('output1')



sheet_name = sys.argv[1] #"Dogs_camp"
sheet_size = sys.argv[2] #"A1:C77"
sheet_n = sheet_name+"!"+sheet_size
sheet_id = sys.argv[3] #"1TRS10OaVDIuQIvJ62-lvL9HuzCAQZaw8l5TCb0QF3kk"



# key path to google auth
SERVICE_ACCOUNT_FILE = 'input/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = sheet_id
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# verison
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=sheet_n).execute()
#remove [] charectors
values = result.get('values', [])
values

# %%
#convert dict to DataFrame
value = pd.DataFrame(values)


# %%
df = pd.DataFrame(value)


# %%
#remove useless header  (0 1 2 3 ...)
df.columns = df.iloc[0]
df = df[1:]

# %%
sdf = df[['Customer', 'Items sold']]

# %%

#save to csv
sdf.to_csv('output/gsheet.csv')


