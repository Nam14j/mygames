import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

Pac_Man_open = pygame.transform.scale(pygame.image.load("pack_man_drawing-removebg-preview.png").convert_alpha(), (50, 50))
Pac_Man_close = pygame.transform.scale(pygame.image.load("pack_open_drawing-removebg-preview.png").convert_alpha(), (50, 50))

pacman = Pac_Man_open.get_rect(center=(400, 300))
speed = 5
direction = None

maze = [
    pygame.Rect(50, 50, 700, 20),
    pygame.Rect(50, 530, 700, 20),
    pygame.Rect(50, 50, 20, 500),
    pygame.Rect(730, 50, 20, 500),

    pygame.Rect(150, 150, 100, 20),
    pygame.Rect(300, 150, 200, 20),
    pygame.Rect(550, 150, 100, 20),

    pygame.Rect(150, 250, 20, 100),
    pygame.Rect(630, 250, 20, 100),

    pygame.Rect(300, 250, 200, 20),
    pygame.Rect(300, 350, 200, 20),

    pygame.Rect(200, 400, 100, 20),
    pygame.Rect(500, 400, 100, 20),

    pygame.Rect(375, 450, 50, 20),
]

clock = pygame.time.Clock()
running = True
mouth_open = True
mouth_counter = 0
mouth_delay = 10

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

    old_pos = pacman.copy()

    if direction == "LEFT":
        pacman.x -= speed
    elif direction == "RIGHT":
        pacman.x += speed
    elif direction == "UP":
        pacman.y -= speed
    elif direction == "DOWN":
        pacman.y += speed

    for wall in maze:
        if pacman.colliderect(wall):
            pacman = old_pos
            break

    mouth_counter += 1
    if mouth_counter >= mouth_delay:
        mouth_open = not mouth_open
        mouth_counter = 0

    if mouth_open:
        current_img = Pac_Man_open
    else:
        current_img = Pac_Man_close

    if direction == "RIGHT" or direction is None:
        rotated_img = current_img
    elif direction == "LEFT":
        rotated_img = pygame.transform.flip(current_img, True, False)
    elif direction == "UP":
        rotated_img = pygame.transform.rotate(current_img, 90)
    elif direction == "DOWN":
        rotated_img = pygame.transform.rotate(current_img, -90)

    screen.fill((0, 0, 0))
    for wall in maze:
        pygame.draw.rect(screen, (0, 0, 255), wall)
    screen.blit(rotated_img, pacman.topleft)
    pygame.display.flip()

pygame.quit()
