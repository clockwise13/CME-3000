import config
from config import *

def main():
    quit_flag = False
    EKRAN = helpers.displayer()
    spawner = classes.Spawn("Peon", (config.res_x/1.5, config.res_y/3), 50, 50)
    spawner.activate()

    fpsClock = pygame.time.Clock()
    FPS = 60
    while quit_flag == False:
        EKRAN.fill(config.WHITE)
        spawner.spawning()
        for event in config.pygame.event.get():
            # simple event handler for testing
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    obj.go_left()
                elif event.key == K_RIGHT:
                    obj.go_right()
                elif event.key == K_p:
                    obj = classes.Peon()
                    obj.rect.x = res_x / 2
                    obj.rect.y = res_y / 2
                elif event.key == K_s:
                    spawner.spawning()
                elif event.key == K_ESCAPE:
                    config.quitter()
            elif event.type == QUIT:
                # added this in to allow for "external" closing of the game
                config.quitter()

        Peon_list.update()
        Peon_list.draw(EKRAN)
        
        # finalise the loop
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
