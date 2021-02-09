import os
from src.custom_dependencies.todoist.api import TodoistAPI

TODOIST_KEY= os.getenv('TODOIST_KEY')
td = TodoistAPI(TODOIST_KEY)
td.sync()

def createSharedProject(project_name, shared_email):
    '''
    Creates a New Project in Todoist and 
    '''
    project = td.projects.add(project_name)
    project.share(shared_email)
    td.commit()
    return project['id']

def addTaskList(project_id, task_list):
    '''
    Adds a new task to a project
    '''

    for task_name in task_list:
        td.items.add(task_name, project_id=project_id)
    
    td.commit()