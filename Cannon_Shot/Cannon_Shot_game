import pygame
import random
import math

asteroid_hit_laser = 0
asteroid_count = 4

screen_width, screen_height = 800, 600
cannon_width, cannon_height = 100, 150

cannon_x = (screen_width - cannon_width) // 7
cannon_y = (screen_height - cannon_height) // 2 + 175
cannon_angle = 0

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cannon Shot")
font = pygame.font.SysFont('Arial', 48)

cannon = pygame.image.load("Cannon.png").convert_alpha()
cannon = pygame.transform.scale(cannon, (150, 100))
asteroid_img = pygame.image.load("asteroid.png").convert_alpha()
asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))

clock = pygame.time.Clock()
running = True
game_over = False
start_ticks = pygame.time.get_ticks()

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

class Laser:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.rect = pygame.Rect(self.x, self.y, 5, 10)

    def update(self):
        self.x += self.sx
        self.y += self.sy
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


lasers = []
asteroids = []

for i in range(asteroid_count):
    asteroid_y = random.randint(-600, -10)
    asteroid_speed = random.randint(3, 6)
    asteroids.append(Asteroid(asteroid_y, asteroid_speed))

while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    cannon_x = (screen_width - cannon.get_width()) // 2
                    cannon_y = (screen_height - cannon.get_height()) // 2 + 175
                    asteroids = []
                    for i in range(asteroid_count):
                        asteroid_y = random.randint(-600, -10)
                        asteroid_speed = random.randint(3, 6)
                        asteroids.append(Asteroid(asteroid_y, asteroid_speed))
                    lasers = []
                    start_ticks = pygame.time.get_ticks()
                    asteroid_hit_laser = 0
                    cannon_angle = 0
                    game_over = False
                elif event.key == pygame.K_q:
                    running = False
            else:
                if event.key == pygame.K_SPACE:
                    theta = math.radians(-cannon_angle)
                    laser_x = cannon_center[0]
                    laser_y = cannon_center[1]
                    speed = 10
                    sx = speed * math.cos(theta)
                    sy = speed * math.sin(theta)
                    lasers.append(Laser(laser_x, laser_y, sx, sy))

    if not game_over:
        if keys[pygame.K_LEFT]:
            cannon_angle += 2
        if keys[pygame.K_RIGHT]:
            cannon_angle -= 2

    for asteroid in asteroids:
        asteroid.update()

    for laser in lasers[:]:
        laser.update()
        if laser.y < 0:
            lasers.remove(laser)
        else:
            for asteroid in asteroids[:]:
                if laser.rect.colliderect(asteroid.rect):
                    asteroid_hit_laser += 1
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

    cannon_center = (cannon_x + cannon.get_width() // 2, cannon_y + cannon.get_height() // 2)
    rotated_cannon = pygame.transform.rotate(cannon, cannon_angle)
    rot_rect = rotated_cannon.get_rect(center=cannon_center)
    screen.blit(rotated_cannon, rot_rect)
    cannon_rect = rot_rect

    for asteroid in asteroids:
        if asteroid.rect.colliderect(cannon_rect):
            game_over = True
            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000

    if game_over:
        text_surface = font.render (f'You lose! R to reset Q to quit , Your time: {elapsed_seconds}s', True, (255, 255, 0))
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)

    score_text = font.render(f"Destroyed: {asteroid_hit_laser}", True, (255, 255, 255))
    score_rect = score_text.get_rect(topright=(screen_width - 10, 10))
    screen.blit(score_text, score_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
