'''
Dummy file to setup rolls
'''

from src.coach_timesheets.timesheets_main import timesheetsMain
from src.read_rolls.read_main import readRolls
from src.setup_rolls.setup_main import setupRolls


text = input("Input 0 for setup, 1 for read, and any other for reading latest timesheet\n")
if text == "0":
    setupRolls()
elif text == "1":
    readRolls()
else:
    timesheetsMain()