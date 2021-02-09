'''
Document that holds all the interactions with the airtable API
'''

import os
import json
import airtable

# define auth in environment
AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
RUSE_DEBATING_PROGRAM_ID = os.getenv('RUSE_DEBATING_PROGRAM_ID')

at = airtable.Airtable(RUSE_DEBATING_PROGRAM_ID, AIRTABLE_KEY)

def _normify(input_dict):
    ''' removes ordered dicts '''
    return json.loads(json.dumps(input_dict))

def returnAllRecords(table_name):
    '''
    Returns all the students that are in the airtable system
    '''

    records = []

    # get the initial 100 results
    returned_records_page = _normify(at.get(table_name=table_name, limit=100))
    offset = returned_records_page.get('offset')

    # get a list of the records
    records = returned_records_page.get('records')
    if records:
        records = records

    # while there are further results, request them
    while(offset):
        returned_records_page = _normify(at.get(table_name=table_name, limit=100, offset=offset))
        offset = returned_records_page.get('offset')

        # if there are additional records, add them to students
        records = returned_records_page.get('records')
        if records:
            records = records + records
    return records

def getRecord(table_name, record_id):
    '''
    returns a dictionary with the record specified

    There will always only be one record
    '''
    try:
        record = _normify(at.get(table_name=table_name, record_id=record_id))
        return record
    except:
        raise Exception('Record_ID does not exist')

def createNewWeek():
    ''' simple function to create a new week '''
    return _normify(at.create('Weeks', {}))

def createNewRollEntry(week_id, class_id, coach_id, student_id_list):
    ''' creates a new roll entry for coach and students '''

    new_entry = {
        "Week": [week_id],
        "Class": [class_id],
        "Coach": [coach_id],
        "Students Attended": student_id_list
    }

    at.create('Overall Rolls', new_entry)
