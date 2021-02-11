import pickle
from googleapiclient.discovery import build

with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)

gsheets = build('sheets', 'v4', credentials=creds)

def addTimesheet(start_time, end_time, duration, date, coach, _class):

    PAYSHEETID = '13MXDrWwn8mKS4yYn8JmzA6uQq5l5LF6Frsr5RAgJrVk'

    gsheets.spreadsheets().values().append(
        spreadsheetId = PAYSHEETID,
        range = 'Sheet1',
        valueInputOption = "RAW",
        insertDataOption = 'INSERT_ROWS',
        includeValuesInResponse = False,
        responseValueRenderOption = 'UNFORMATTED_VALUE',
        responseDateTimeRenderOption = 'SERIAL_NUMBER',
        body = {
            'range': 'Sheet1',
            'values': [[
                date,
                coach,
                _class, 
                start_time,
                end_time,
                duration
            ]]
        }
    ).execute()