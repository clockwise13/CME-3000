import config
from config import *

def main():
    quit_flag = False
    EKRAN = helpers.displayer()
    peon = classes.Peon()
    #Head = classes.Head()

    peon.rect.x = res_x / 2
    peon.rect.y = res_y / 2

    fpsClock = pygame.time.Clock()
    FPS = 60
    while quit_flag == False:
        EKRAN.fill(config.WHITE)
        for event in config.pygame.event.get():
            # simple event handler for testing
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    peon.go_left()
                elif event.key == K_RIGHT:
                    peon.go_right()
                elif event.key == K_p:
                    peon = classes.Peon()
                    peon.rect.x = res_x / 2
                    peon.rect.y = res_y / 2
                elif event.key == K_ESCAPE:
                    config.quitter()
            elif event.type == QUIT:
                # added this in to allow for "external" closing of the game
                config.quitter()

        Peon_list.update()
        #Head_list.update()
        Peon_list.draw(EKRAN)
        #Head_list.draw(EKRAN)

        # finalise the loop
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
