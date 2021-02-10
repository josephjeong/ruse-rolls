'''
main file that reads rolls and marks attendance
'''

from src.api_clients.todoist_client import getAllProjects


def readRolls():
    ''' main function to read rolls '''

    projects = getAllProjects()

    for project in projects:
        if not project: continue

        print(project.get('data').get('id'))