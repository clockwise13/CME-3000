import config
from config import *

EKRAN = config.helpers.displayer()
EKRAN.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
h = classes.Head()
FPS = 30

while __name__ == '__main__':
    for event in config.pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                config.quitter()
            elif event.key == K_SPACE:
                EKRAN.fill((255, 255, 255))
            else:
                p = classes.Peon()
        elif event.type == QUIT:
            # added this in to allow for "external" closing of the game
            config.quitter()

    EKRAN.fill((255, 255, 255))
    config.helpers.collider(h) # a call to the collider function to check for Head vs. Peons collisions

    # updaters and draw calls for Peon and Head lists; to be depraciated in favor of a snazzy loop or list comprehension handler

    config.Head_list.update()
    config.Peon_list.update()
    config.Head_list.draw(EKRAN)
    config.Peon_list.draw(EKRAN)

    # finalise the loop
    config.pygame.display.update()
    fpsClock.tick(FPS)
