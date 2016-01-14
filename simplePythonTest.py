import config
from config import *

while __name__ == '__main__':

    EKRAN = helpers.displayer()
    EKRAN.fill(config.WHITE)

    peon = classes.Peon()
    #Head = classes.Head()

    peon.rect.x = res_x / 2
    peon.rect.y = res_y / 2

    fpsClock = pygame.time.Clock()
    FPS = 60
    
    for event in config.pygame.event.get():
        
        #moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                peon.go_left()
            if event.key == pygame.K_RIGHT:
                peon.go_right()
        
        #stopping
        
             
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                config.quitter()
        elif event.type == QUIT:
            # added this in to allow for "external" closing of the game
            config.quitter()

    Peon_list.update()
    #Head_list.update()
    
    ''' Attempts at automatic movement:
    if peon.rect.right >= res_x:
        peon.direction == "L"
        peon.change_x = -6
        
    if peon.rect.left <= 0:
        peon.direction == "R"
        peon.change_x = 6
    '''


    Peon_list.draw(EKRAN)
    #Head_list.draw(EKRAN)

    # finalise the loop
    fpsClock.tick(FPS)
    pygame.display.flip()
