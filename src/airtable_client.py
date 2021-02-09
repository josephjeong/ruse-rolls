import os
from airtable import Airtable

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
RUSE_DEBATING_PROGRAM_ID = os.getenv('RUSE_DEBATING_PROGRAM_ID')

print(AIRTABLE_KEY, RUSE_DEBATING_PROGRAM_ID)

base_students = Airtable(RUSE_DEBATING_PROGRAM_ID, 'Students', AIRTABLE_KEY)

print(base_students.get_all())