'''
main file that invokes the program to start
'''
from src.api_clients.todoist_client import addTaskList, createSharedProject
from src.api_clients.airtable_client import createNewWeek, returnAllRecords

def setupRolls():

    # create a new week
    new_week = createNewWeek()
    week_number = new_week.get('fields').get('Auto-Week Number')

    # get all the classes returned
    classes = returnAllRecords('Classes')

    # get the roll-names in each class
    for _class in classes:
        roll_names = _class.get('fields').get('Roll-Names')

        # if there is nobody in a class
        if not roll_names:
            continue

        # get the coach details to share
        coach_email = _class.get('fields').get('Coach Email')
        coach_name = _class.get('fields').get('Coach Name')
        room = _class.get('fields').get('Room Name')
        print(coach_email)

        # create roll and share with coach
        roll_name = str(week_number) + " " + str(coach_name[0]) + " " + str(room[0])
        project_id = createSharedProject(roll_name, 'joseph.b.jeong@gmail.com')

        # add all roll-names to src.custom_dependencies.todoist rolls
        addTaskList(project_id, roll_names)

    return 'lmao'
