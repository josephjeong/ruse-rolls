'''
Dummy file to setup rolls
'''

from src.setup_rolls.setup_main import setupRolls


text = input("Input 0 for setup, 1 for read\n")
if text == "0":
    setupRolls()
else:
    print('lmao')