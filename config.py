# config module with global imports and values

import sys
import os
import pygame
import math
import random
import cPickle
import classes
import helpers
import numpy

from pygame.locals import *
from helpers import *

# GLOBALS

res_x = 1280
res_y = 720

BLACK    = (0, 0, 0)
WHITE    = (255, 255, 255)
BLUE     = (0, 0, 255)

# image sizes, format: (height, width)

wall_size = (70, 70)

#containers for sprite objects using the sprite.Group() class
Peon_list = pygame.sprite.Group()
Head_list = pygame.sprite.Group()
Object_list = pygame.sprite.Group() # only call update() on this one!
GUI_list = pygame.sprite.Group()

# dummy counter for dummy counting

dummy_counter = 0

# INITS

pygame.init()
pygame.mixer.init()
