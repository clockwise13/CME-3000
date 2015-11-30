import config
from config import *

EKRAN = config.helpers.displayer()
EKRAN.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
FPS = 10

while True:
    for event in config.pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                config.quitter()
            elif event.key == K_SPACE:
                EKRAN.fill((255, 255, 255))
                for thing in config.Peon_list:
                    thing.mover()
                    config.helpers.blitter(EKRAN, thing.image, thing.pos)
            else:
                p = classes.Peon()
                config.helpers.blitter(EKRAN, p.image, p.pos)
            config.pygame.display.update()
            print
            print p, p.pos

