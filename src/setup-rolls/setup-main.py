'''
main file that invokes the program to start
'''
import json

from src.airtable_client import returnAllRecords

def setupRolls():
    # get all the classes returned
    classes = json.loads(json.dumps(returnAllRecords('Classes')))

    # get the roll-names in each class
    for _class in classes:
        roll_names = _class.get('fields').get('Roll-Names')

        # if there is nobody in a class
        if not roll_names:
            continue

        # add all roll-names to todoist rolls
        for roll_name in roll_names:
            
