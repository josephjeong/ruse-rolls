'''
main file that reads rolls and marks attendance
'''

from src.api_clients.airtable_client import getLatestWeek, searchRollsByTodoistId, updateRolls
from src.api_clients.todoist_client import getAllProjects, getAllTasks, archiveRolls

from pprint import PrettyPrinter

pp = PrettyPrinter(indent = 4)

def readRolls():
    ''' main function to read rolls '''

    latest_week = getLatestWeek()
    projects = getAllProjects()

    for project in projects:
        if not project: continue

        project_id = project.get('data').get('id')

        rolls = getAllTasks(project_id)
        roll_record = (searchRollsByTodoistId(rolls.get('project').get('id')).get('records'))
        if not roll_record: continue
        roll_record = roll_record[0]
        print(roll_record)
        
        students_present = []
        students_absent = []

        for student in rolls.get('items'):
            student_roll_name =  student.get('content')
            student_record_id = student_roll_name[-17:]
            student_present = student.get('checked')
            
            if student_present:
                students_present.append(student_record_id)
            else:
                students_absent.append(student_record_id)
        
        update_data = {
            "Students Attended": students_present,
            "Students Absent": students_absent
        }

        updateRolls(roll_record['id'], update_data)
        archiveRolls(project_id)



