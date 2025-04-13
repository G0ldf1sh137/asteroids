import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *


def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Group assignments
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    # Sprites
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    

    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update Objects positions
        for obj in updatable:
            obj.update(dt)
            
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                return
            
            for shot in shots:
                if a.collides_with(shot):
                    a.split()
                    shot.kill()

        # Blank out the screen
        screen.fill('black')
        
        # Draw sprites
        for obj in drawable:
            obj.draw(screen)
         
        # Flip Display
        pygame.display.flip()
        
        # Tick clock and calculate dt
        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()