import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    dt = 0 
    pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()     
        screen.fill("black")
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()
