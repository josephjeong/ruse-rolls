''' python script to fill in coach timesheets from latest week '''

from src.api_clients.sheets_client import addTimesheet
from src.api_clients.airtable_client import getLatestWeek, getRecord

def timesheetsMain():
    current_week = getLatestWeek().get('records')[0].get('fields')

    for rolls_id in current_week.get('Overall Rolls'):
        rolls = getRecord('Overall Rolls', rolls_id).get('fields')

        addTimesheet(
            start_time = rolls.get('Start Time (from Time Slot) (from Class)')[0],
            end_time = rolls.get('End Time (from Time Slot) (from Class)')[0],
            duration = rolls.get('Duration (from Time Slot) (from Class)')[0],
            date = rolls.get('Date (from Week)')[0],
            coach = rolls.get('Coach Name (from Coach)')[0],
            _class = rolls.get('Name')
        )
