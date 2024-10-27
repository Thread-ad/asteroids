import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
from shots import *




def main():
    pygame.init()
    clock = pygame.time.Clock()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)
    

    ship = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return

            
        for unit in updatable:
            unit.update(dt)

        screen.fill((0,0,0))

        for unit in drawable:
            unit.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if ship.collision(asteroid):
                print(f"Game over man!")
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        


   
if __name__ == "__main__":
    main()
