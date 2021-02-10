'''
main file that reads rolls and marks attendance
'''

import re

from src.api_clients.airtable_client import getLatestWeek, searchRollsByTodoistId, updateRolls
from src.api_clients.todoist_client import getAllProjects, getAllTasks, archiveRolls

def searchRecordId(roll_name):
    record_id = re.search('(rec.{14})', roll_name)
    if not record_id: return None
    record_id = record_id.group(0)
    return record_id

def readRolls():
    ''' main function to read rolls '''

    projects = getAllProjects()

    for project in projects:
        if not project: continue

        project_id = project.get('data').get('id')

        # get the rolls stored in todoist
        rolls = getAllTasks(project_id)

        # get the rolls stored in airtable that correspond to the ones in todoist
        roll_record = (searchRollsByTodoistId(rolls.get('project').get('id')).get('records'))
        if not roll_record: continue
        roll_record = roll_record[0]

        # everyone defaults to absent in rolls
        # now we're going to default them all to present, and subtract them one by one
        students_present = roll_record.get('fields').get('Students Absent')
        students_absent = []

        # if student is in the rolls, they are present 
        for student in rolls.get('items'):
            student_roll_name =  student.get('content')
            student_record_id = searchRecordId(student_roll_name)
            if not student_record_id: continue
            
            try:
                students_present.remove(student_record_id)
            except ValueError: continue
            students_absent.append(student_record_id)
        
        update_data = {
            "Students Attended": students_present,
            "Students Absent": students_absent,
            "Rolls Completed": True
        }

        print(update_data)

        updateRolls(roll_record['id'], update_data)
        archiveRolls(project_id)



