# this module will create an instance of the level class and serialize it using pickle

import pickle
import config
from config import *

# Creating object_dict

Objects_dict = {'Head': None, 'Peon' = None, 'Spawner' = None}

# Creating GUI_dict for storing interface objects

GUI_dict = {'Buttons' = None, 'Panes' = None, 'TextBoxes' = None, 'Meters' = None}

# Creating miscalenous objects dictionary

Misc_dict = {'Background' = None}

# Creating music dictionary

Music_dict = {'Ambient' = None, 'Opening' = None, 'Victory' = None}

# Create objects for the object_dict

#Head = classes.Head()
#config.Head_list.append(Head)
#config.Object_list.append(Head)
Peon_spawner = classes.Spawn("Peon", ((config.res_x/4, config.res_y/3)), 20)

# Creating GUI objects

# Creating misc objects

Misc_dict['Background' = config.WHITE]

# Initial peons?
"""Peon_num = 8
for n in range(1, Peon_num, step=1):
    p = classes.Peon()
    config.Peon_list.append(p)
    config.Object_list.append(p)"""

# Add objects to dictionary

# print statements for testing purposes

print Objects_dict
print

print GUI_dict
print

print Misc_dict
print

# create level instance for pickling further down the line

level_name = raw_input(prompt="Name the level you want to create: ")
level_name = classes.Level_creator(Misc_dict, object_dict, GUI_dict, Music_dict)
