# this module will create an instance of the level class and serialize it using pickle

import pickle
import config
from config import *

# Create object_dict

Objects = {'Head': None, 'Peon' = None, 'Spawner' = None}

# Create objects for the object_dict

Head = classes.Head()
config.Head_list(Head)
config.Object_list(Head)
# Initial peons?
Peon_num = 8
for n in range(1, Peon_num, step=1):
    p = classes.Peon()
    config.Peon_list.append(p)
    config.Object_list.append(p)

# Spawners for spawnable objects

Peon_spawner = classes.Spawn("Peon", ((config.res_x/4, config.res_y/3)), 20)

# Add objects to dictionary

"""Will the keys of the dict be lists? Can I use lists? Answer: YES I CAN"""
