# config module with global imports and values

print __name__

import sys
import pygame
import math
import random
import classes
import helpers

from pygame.locals import *
from helpers import *

# GLOBALS

res_x = 1280
res_y = 720

Peon_list = []
Head_list = []
Object_list = [Peon_list, Head_list]
dummy_counter = 0

# INITS

pygame.init()
