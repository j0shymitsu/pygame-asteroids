import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

    # init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # FPS
    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while(True):

        # makes windows close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
        screen.fill('black')
        for item in drawable:
            item.draw(screen)  
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()