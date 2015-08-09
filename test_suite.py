# test module for game


# place to import game files


import classes, config



# GLOBALS




image = "Peon"
from helpers import displayer, blitter
DISPLAY = displayer(config.res_x, config.res_y)
Pizda = classes.Peon((43, 58))
Pizda.Peon_blit((config.res_x/2, config.res_y/2), DISPLAY)
print Pizda

