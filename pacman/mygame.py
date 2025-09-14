import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

Pac_Man_open = pygame.transform.scale(pygame.image.load("pack_man_drawing-removebg-preview.png").convert_alpha(), (25, 25))
Pac_Man_close = pygame.transform.scale(pygame.image.load("pack_open_drawing-removebg-preview.png").convert_alpha(), (25, 25))
Ghost = pygame.transform.scale(pygame.image.load("Ghost-removebg-preview.png").convert_alpha(), (25, 25))

pacman = Pac_Man_open.get_rect(center=(400, 300))
ghost = Ghost.get_rect(center=(200, 200))
speed = 5
direction = None

maze = [
    pygame.Rect(50, 50, 700, 20),
    pygame.Rect(50, 530, 700, 20),
    pygame.Rect(50, 50, 20, 500),
    pygame.Rect(730, 50, 20, 500),
    pygame.Rect(150, 100, 200, 20),
    pygame.Rect(450, 100, 200, 20),
    pygame.Rect(150, 180, 100, 20),
    pygame.Rect(550, 180, 100, 20),
    pygame.Rect(300, 180, 20, 100),
    pygame.Rect(480, 180, 20, 100),
    pygame.Rect(200, 280, 150, 20),
    pygame.Rect(450, 280, 150, 20),
    pygame.Rect(200, 360, 100, 20),
    pygame.Rect(550, 360, 100, 20),
    pygame.Rect(350, 360, 100, 20),
    pygame.Rect(350, 400, 20, 80),
    pygame.Rect(430, 400, 20, 80),
    pygame.Rect(200, 460, 150, 20),
    pygame.Rect(450, 460, 150, 20),
]

dots = []
grid_size = 30
for x in range(70, 730, grid_size):
    for y in range(70, 530, grid_size):
        dot_rect = pygame.Rect(x, y, 8, 8)
        is_valid = True
        for wall in maze:
            if dot_rect.colliderect(wall):
                is_valid = False
                break
        if is_valid:
            dots.append(dot_rect)

clock = pygame.time.Clock()
running = True
mouth_open = True
mouth_counter = 0
mouth_delay = 10
score = 0

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

    for dot in dots[:]:
        if pacman.colliderect(dot):
            dots.remove(dot)
            score += 10

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
    for dot in dots:
        pygame.draw.circle(screen, (255, 255, 0), dot.center, 4)
    screen.blit(rotated_img, pacman.topleft)
    screen.blit(Ghost, ghost.topleft)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
