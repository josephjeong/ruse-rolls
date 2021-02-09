import os
import json
import airtable

# define auth in environment
AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
RUSE_DEBATING_PROGRAM_ID = os.getenv('RUSE_DEBATING_PROGRAM_ID')

# used to help with debug
import pprint
pp = pprint.PrettyPrinter(indent=4)

def returnLimitedStudents():
    base_students = airtable.Airtable(RUSE_DEBATING_PROGRAM_ID, AIRTABLE_KEY)
    # highest limit is 100
    students = json.loads(json.dumps(base_students.get(table_name='Students', limit=100)))
    return students