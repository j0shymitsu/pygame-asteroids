import pygame
from constants import *

def main():
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    # init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while(True):

        # makes windows close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill('black')
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()