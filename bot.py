print("Hello world")

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)

client = gspread.authorize(credentials)

sheet = client.open("Test Spreadsheet").sheet1

data = sheet.get_all_records()
print(data)


