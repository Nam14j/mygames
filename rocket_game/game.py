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
text_surface = font.render('you lose!', True, (255, 255, 0))
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
rocket_img1 = pygame.image.load("rocket.png").convert_alpha()

try:
    rocket_img = pygame.transform.scale(rocket_img1, (new_width, new_height))
except pygame.error:
    print("Error")
    pygame.quit()
    sys.exit()

class Asteroid:    
    def __init__(self, y, speed):
        self.x = random.randint(0, screen_width - asteroid_img.get_width())
        self.y = y
        self.speed = speed
        self.rect = asteroid_img.get_rect(topleft=(self.x, self.y))
    #end method

    def draw(self, screen):
        screen.blit(asteroid_img, (self.x, self.y))
    #end method

    def update(self):
        flag_hit_floor = False

        self.y += self.speed

        if self.y > screen_height:
            flag_hit_floor = True
            self.y = -asteroid_img.get_height()
            self.x = random.randint(0, screen_width - asteroid_img.get_width())
        #end if

        self.rect.topleft = (self.x, self.y)

        return flag_hit_floor
    #end method

#end class

try:
    asteroid_img = pygame.image.load("asteroid.jpg").convert_alpha()
    asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))
except pygame.error:
    print("Error")
    pygame.quit()
    sys.exit()

rocket_img = pygame.transform.scale(rocket_img1, (new_width, new_height))


rocket_x = (screen_width - rocket_img.get_width()) // 2
rocket_y = (screen_height - rocket_img.get_height()) // 2 + 175
rocket_speed = 10
rocket_visible = True


asteroids = []

for i in range(asteroid_count):
    asteroid_y = random.randint(-600, -10)
    asteroid_speed = random.randint(3, 6)
    asteroids.append(Asteroid(asteroid_y, asteroid_speed))

#asteroid_x = random.randint(0, screen_width - asteroid_img.get_width())
asteroid_y = -asteroid_img.get_height()
asteroid_speed = 4

asteroid = Asteroid(asteroid_y, asteroid_speed)

clock = pygame.time.Clock()
running = True
hit_reported = False

while running:
    screen.fill((0, 0, 0))


    if rocket_visible:
        screen.blit(rocket_img, (rocket_x, rocket_y))

    #screen.blit(asteroid_img, (asteroid_x, asteroid_y))
    asteroid.draw(screen)


    rocket_rect = rocket_img.get_rect(topleft=(rocket_x, rocket_y))

    for asteroid in asteroids:
        asteroid.draw(screen)
        asteroid.update()

    #asteroid_rect = asteroid_img.get_rect(topleft=(asteroid_x, asteroid_y))
    flag_hit_floor = asteroid.update()

    #asteroid_y += asteroid_speed

    if flag_hit_floor:
        #asteroid_y = -asteroid_img.get_height()
        #asteroid_x = random.randint(0, screen_width - asteroid_img.get_width())
        hit_reported = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT]:
        rocket_x += rocket_speed
    rocket_x = max(0, min(rocket_x, screen_width - rocket_img.get_width()))


    for asteroid in asteroids:
        if asteroid.rect.colliderect(rocket_rect) and not hit_reported:
            screen.blit(text_surface, text_rect)
            hit_reported = True
            running = False 

    if hit_reported:
        screen.fill((0, 0, 0))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
