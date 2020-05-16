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

sh = client.open("Test Spreadsheet")

worksheet = sh.add_worksheet(title="New ABC 2", rows="100", cols="20")

worksheet.format("A2:B2", {
    "backgroundColor": {
      "red": 0.0,
      "green": 0.0,
      "blue": 0.0
    }
})

