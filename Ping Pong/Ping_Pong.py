import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()


def draw_text(surface, text, position, font_size=32, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)


def make_player_1(player_1_y):
    hitbox = pygame.Rect(50, player_1_y, 10, 100)
    pygame.draw.rect(screen, (255, 255, 255), hitbox)
    return hitbox


def make_player_2(player_2_y):
    hitbox = pygame.Rect(WIDTH - 60, player_2_y, 10, 100)
    pygame.draw.rect(screen, (255, 255, 255), hitbox)
    return hitbox


def make_ball(ball_x, ball_y):
    hitbox = pygame.Rect(ball_x, ball_y, 10, 10)
    pygame.draw.rect(screen, (255, 255, 255), hitbox)
    return hitbox


def draw_score(player_1_score, player_2_score):
    score_text = f"{player_1_score} - {player_2_score}"
    draw_text(screen, score_text, (WIDTH // 2 - 25, 20))


def draw_center_line():
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, (80, 80, 80), (WIDTH // 2 - 1, y, 2, 20))


def reset_ball():
    return Ball(WIDTH // 2 - 5, HEIGHT // 2 - 5)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y <= 0:
            self.y = 0
            self.speed_y *= -1

        if self.y >= HEIGHT - 10:
            self.y = HEIGHT - 10
            self.speed_y *= -1

    def draw(self):
        make_ball(self.x, self.y)


player_1_y = HEIGHT // 2 - 50
player_2_y = HEIGHT // 2 - 50

player_speed = 5
player_2_speed = 5

player_1_score = 0
player_2_score = 0

ball = reset_ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_r:
                player_1_score = 0
                player_2_score = 0
                ball = reset_ball()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_1_y -= player_speed
    if keys[pygame.K_s]:
        player_1_y += player_speed

    if keys[pygame.K_UP]:
        player_2_y -= player_2_speed
    if keys[pygame.K_DOWN]:
        player_2_y += player_2_speed

    player_1_y = max(0, min(HEIGHT - 100, player_1_y))
    player_2_y = max(0, min(HEIGHT - 100, player_2_y))

    ball.move()

    screen.fill((0, 0, 0))

    draw_score(player_1_score, player_2_score)
    draw_center_line()

    player_1_hitbox = make_player_1(player_1_y)
    player_2_hitbox = make_player_2(player_2_y)

    ball_hitbox = pygame.Rect(ball.x, ball.y, 10, 10)

    if ball_hitbox.colliderect(player_1_hitbox) and ball.speed_x < 0:
        ball.x = player_1_hitbox.right
        offset = (ball.y + 5) - player_1_hitbox.centery
        ball.speed_y = offset * 0.15
        ball.speed_x *= -1

    if ball_hitbox.colliderect(player_2_hitbox) and ball.speed_x > 0:
        ball.x = player_2_hitbox.left - 10
        offset = (ball.y + 5) - player_2_hitbox.centery
        ball.speed_y = offset * 0.15
        ball.speed_x *= -1

    if ball.x <= 0:
        player_2_score += 1
        ball = reset_ball()

    if ball.x >= WIDTH - 10:
        player_1_score += 1
        ball = reset_ball()

    ball.draw()

    pygame.display.flip()
    clock.tick(60)