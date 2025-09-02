import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

Pac_Man_open = pygame.image.load("pack_man_drawing-removebg-preview.png").convert_alpha()
Pac_Man_close = pygame.image.load("pack_open_drawing-removebg-preview.png").convert_alpha()
Pac_Man_open = pygame.transform.scale(Pac_Man_open, (62, 62))
Pac_Man_close = pygame.transform.scale(Pac_Man_close, (62, 62))


x, y = 400, 300
speed = 5
mouth_open = True
clock = pygame.time.Clock()
running = True
mouth_counter = 0
mouth_delay = 10
direction = "RIGHT"

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        x += speed
        direction = "RIGHT"
    if keys[pygame.K_UP]:
        y -= speed
        direction = "UP"
    if keys[pygame.K_DOWN]:
        y += speed
        direction = "DOWN"


    mouth_counter += 1
    if mouth_counter >= mouth_delay:
        mouth_open = not mouth_open
        mouth_counter = 0

    if mouth_open:
        current_img = Pac_Man_open
    else:
        current_img = Pac_Man_close

    if direction == "RIGHT":
        rotated_img = current_img
    elif direction == "LEFT":
        rotated_img = pygame.transform.flip(current_img, True, False)
    elif direction == "UP":
        rotated_img = pygame.transform.rotate(current_img, 90)
    elif direction == "DOWN":
        rotated_img = pygame.transform.rotate(current_img, -90)

    screen.fill((0, 0, 0))
    screen.blit(rotated_img, (x, y))
    pygame.display.flip()

pygame.quit()
