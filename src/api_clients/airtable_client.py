'''
Document that holds all the interactions with the airtable API
'''

import os
import airtable

from src.api_clients.normify import normify

# define auth in environment
AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
RUSE_DEBATING_PROGRAM_ID = os.getenv('RUSE_DEBATING_PROGRAM_ID')

at = airtable.Airtable(RUSE_DEBATING_PROGRAM_ID, AIRTABLE_KEY)

def returnAllRecords(table_name):
    '''
    Returns all the students that are in the airtable system
    '''

    records = []

    # get the initial 100 results
    returned_records_page = normify(at.get(table_name=table_name, limit=100))
    offset = returned_records_page.get('offset')

    # get a list of the records
    records = returned_records_page.get('records')
    if records:
        records = records

    # while there are further results, request them
    while(offset):
        returned_records_page = normify(at.get(table_name=table_name, limit=100, offset=offset))
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
        record = normify(at.get(table_name=table_name, record_id=record_id))
        return record
    except:
        raise Exception('Record_ID does not exist')

def createNewWeek():
    ''' simple function to create a new week '''
    return normify(at.create('Weeks', {}))

def createNewRollEntry(week_id, class_id, coach_id, todoist_id):
    ''' creates a new roll entry for coach and students '''

    new_entry = {
        "Week": [week_id],
        "Class": [class_id],
        "Coach": [coach_id],
        "todoist-roll-id": todoist_id
    }

    at.create('Overall Rolls', new_entry)

def getLatestWeek():
    ''' 
    gets the latest record created from airtable 
    
    returns object in this format:
    {
        'records': [
            {'id': 'recYAe0G9splUuHxa', 
            'fields': {
                'Auto-Week Number': 3, 
                'Overall Rolls': [
                    'recY5lGoaqU0kIdm8', 
                    'reciIdKOKRHnizy7L', 
                    'receWMRZwy9viDcYY', 
                    'rec2mkU1TeRw3lEQH', 
                    'reclqDSBhTmDLiLN2', 
                    'recqMrl1C9izgHfKT', 
                    'recQdLPP2Owh7Qtp0', 
                    'rec2vmu9bxhQzs0Np', 
                    'recmine3DYfFBnbFN', 
                    'recx5GUVwYfkpjV0U', 
                    'recDdZNKUgERdJN3j', 
                    'rec3ltEa2G9Bn9xLn', 
                    'recnDbVJpteY8mLS4', 
                    'recAov9u92r7pHv2b'], 
                'Week': 'Week 3 - 09 Feb - 16 Feb 2021', 
                'Created': '2021-02-09', 
                'Calculation': 'recYAe0G9splUuHxa'
                }, 
                'createdTime': '2021-02-09T08:21:25.000Z'
            }
        ]
    }
    '''

    return normify(at.get('Weeks', max_records=1, view='LatestWeek'))

def searchRollsByTodoistId(todoist_id):
    return normify(at.get('Overall Rolls',
        max_records=1, 
        filter_by_formula='{todoist-roll-id}=' + str(todoist_id)
        ))

def updateRolls(record_id, data):
    at.update(table_name='Overall Rolls', record_id=record_id, data=data)