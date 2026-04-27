#lib
import pygame
import sys

#modules
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #Object instances
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    
    #Start game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        updatable.update(dt)
        p1.shot_cooldown -= dt
        for a in asteroids:
            if a.collides_with(p1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
