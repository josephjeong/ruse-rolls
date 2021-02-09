'''
Document that holds all the interactions with the airtable API
'''

import os
import json
import airtable

# define auth in environment
AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
RUSE_DEBATING_PROGRAM_ID = os.getenv('RUSE_DEBATING_PROGRAM_ID')

# used to help with debug
import pprint
pp = pprint.PrettyPrinter(indent=4)

at = airtable.Airtable(RUSE_DEBATING_PROGRAM_ID, AIRTABLE_KEY)

def returnAllRecords(table_name):
    '''
    Returns all the students that are in the airtable system
    '''

    records = []

    # get the initial 100 results
    returned_records_page = json.loads(json.dumps(at.get(table_name=table_name, limit=100)))
    offset = returned_records_page.get('offset')

    # get a list of the records
    records = returned_records_page.get('records')
    if records:
        records = records

    # while there are further results, request them
    while(offset):
        returned_records_page = json.loads(json.dumps(at.get(table_name=table_name, limit=100, offset=offset)))
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
        record = json.loads(json.dumps(at.get(table_name=table_name, record_id=record_id)))
        return record
    except:
        raise Exception('Record_ID does not exist')
