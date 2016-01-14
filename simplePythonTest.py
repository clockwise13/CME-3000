import config
from config import *

EKRAN = helpers.displayer()
#EKRAN.fill((255, 255, 255))


Peon = classes.Peon()
#Head = classes.Head()



Peon.rect.x = res_x / 2
Peon.rect.y = res_y / 2

fpsClock = pygame.time.Clock()
FPS = 60

while __name__ == '__main__':
    for event in config.pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                config.quitter()
        elif event.type == QUIT:
            # added this in to allow for "external" closing of the game
            config.quitter()

    Peon_list.update()
    #Head_list.update()
    
    if Peon.rect.right >= res_x:
        Peon.direction == "L"
        Peon.change_x = -6
        
    if Peon.rect.left <= 0:
        Peon.direction == "R"
        Peon.change_x = 6

    #EKRAN.fill((255, 255, 255))

    Peon_list.draw(EKRAN)
    #Head_list.draw(EKRAN)

    # finalise the loop
    fpsClock.tick(FPS)
    pygame.display.flip()
