import pygame
import sys
import random

new_width = 100
new_height = 100
asteroid_count = 4

pygame.init()
pygame.font.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Ship Viewer")
font = pygame.font.SysFont('Arial', 48)

rocket_img1 = pygame.image.load("rocket.png").convert_alpha()
rocket_img = pygame.transform.scale(rocket_img1, (new_width, new_height))

asteroid_img = pygame.image.load("asteroid.png").convert_alpha()
asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))

class Asteroid:    
    def __init__(self, y, speed):
        self.x = random.randint(0, screen_width - asteroid_img.get_width())
        self.y = y
        self.speed = speed
        self.rect = asteroid_img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(asteroid_img, (self.x, self.y))

    def update(self):
        if self.y > screen_height:
            self.y = -asteroid_img.get_height()
            self.x = random.randint(0, screen_width - asteroid_img.get_width())
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

rocket_x = (screen_width - rocket_img.get_width()) // 2
rocket_y = (screen_height - rocket_img.get_height()) // 2 + 175
rocket_speed = 10

class Laser:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x, y, 5, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def update(self):
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y)

lasers = []
asteroids = []
for i in range(asteroid_count):
    asteroid_y = random.randint(-600, -10)
    asteroid_speed = random.randint(3, 6)
    asteroids.append(Asteroid(asteroid_y, asteroid_speed))

clock = pygame.time.Clock()
running = True
game_over = False
start_ticks = pygame.time.get_ticks()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    rocket_x = (screen_width - rocket_img.get_width()) // 2
                    rocket_y = (screen_height - rocket_img.get_height()) // 2 + 175
                    asteroids = []
                    for i in range(asteroid_count):
                        asteroid_y = random.randint(-600, -10)
                        asteroid_speed = random.randint(3, 6)
                        asteroids.append(Asteroid(asteroid_y, asteroid_speed))
                    lasers = []
                    start_ticks = pygame.time.get_ticks()
                    game_over = False
                elif event.key == pygame.K_q:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    laser_x = rocket_x + rocket_img.get_width() // 2 - 2
                    laser_y = rocket_y
                    lasers.append(Laser(laser_x, laser_y, 10))

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rocket_x -= rocket_speed
        if keys[pygame.K_RIGHT]:
            rocket_x += rocket_speed
        rocket_x = max(0, min(rocket_x, screen_width - rocket_img.get_width()))

        rocket_rect = rocket_img.get_rect(topleft=(rocket_x, rocket_y))
        for asteroid in asteroids:
            asteroid.update()
            if asteroid.rect.colliderect(rocket_rect):
                game_over = True
                elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000

        for laser in lasers[:]:
            laser.update()
            if laser.y < 0:
                lasers.remove(laser)
            else:
                for asteroid in asteroids[:]:
                    if laser.rect.colliderect(asteroid.rect):
                        asteroids.remove(asteroid)
                        lasers.remove(laser)
                        new_y = random.randint(-600, -10)
                        new_speed = random.randint(3, 6)
                        asteroids.append(Asteroid(new_y, new_speed))
                        break

    for asteroid in asteroids:
        asteroid.draw(screen)

    for laser in lasers:
        laser.draw(screen)

    screen.blit(rocket_img, (rocket_x, rocket_y))

    if game_over:
        text_surface = font.render(
            f'You lose! R to reset Q to quit , Your time: {elapsed_seconds}s',
            True,
            (255, 255, 0)
        )
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
