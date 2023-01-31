# %%
from __future__ import print_function
import os.path
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account

# check the folder exist or not
import os
if not os.path.exists('output'):
   os.makedirs('output')



# key path to google auth
SERVICE_ACCOUNT_FILE = 'input/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '17ArB6sfNCO11qqIsfZr2I4HEw-FBEw0jiY7Cin_u-Ew'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# verison
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Dogs campaign!A1:J77").execute()
#remove [] charectors
values = result.get('values', [])


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


