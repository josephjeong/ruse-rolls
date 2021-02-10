import os
from todoist.api import TodoistAPI

# from src.api_clients.normify import normify

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
        print(task_name)
        td.items.add(task_name, project_id=project_id)
    
    td.commit()

def getAllProjects():
    ''' 
    gets all projects from todoist
    
    Type Project looks like this:
    Project({'child_order': 47,
    'collapsed': 0,
    'color': 47,
    'id': 2257918677,
    'is_archived': 0,
    'is_deleted': 0,
    'is_favorite': 0,
    'name': '3 Arshad _Aman_ Mohamed Library Room 2',
    'parent_id': None,
    'shared': True,
    'sync_id': 8355925})
    
     '''

    # get the project list from the synced projects
    td.sync()
    project_list = td['projects']

    normified_project_list = []

    # normify the projects
    for project in project_list:
        if not project: continue
            
        # create the normified dict
        normified_project_list.append(vars(project))
    
    return normified_project_list
