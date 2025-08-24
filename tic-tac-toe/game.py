import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tik-Tak-Toe")
font = pygame.font.SysFont("Arial", 24)


win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


class Box:
    def __init__(self, x, y, height, width, index):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.index = index
        self.state = 0
        self.color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 3)
        if self.state == 1:
            text_surface = font.render("X", True, BLACK)
            surface.blit(text_surface, (self.x + self.width // 3, self.y + self.height // 4))
        elif self.state == 2:
            text_surface = font.render("O", True, BLACK)
            surface.blit(text_surface, (self.x + self.width // 3, self.y + self.height // 4))

    def does_have_point(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height

boxes = []
index = 0
for y in range(0, 150, 50):
    for x in range(0, 150, 50):
        boxes.append(Box(x, y, 50, 50, index))
        index += 1


reset_box = Box(200, 200, 40, 100, -1)
reset_box.color = BLACK

def draw_reset_button():
    reset_box.draw(screen)
    reset_text = font.render("RESET", True, BLACK)
    reset_rect = reset_text.get_rect(center=(reset_box.x + 50, reset_box.y + 20))
    screen.blit(reset_text, reset_rect)


def full_reset():
    for box in boxes:
        box.state = 0
        box.color = BLACK


def click():
    message = ""
    for box in boxes:
        if box.does_have_point() and box.state == 0:
            count = sum(1 for b in boxes if b.state != 0)
            box.state = 1 if count % 2 == 0 else 2
            break

    winner_found = False
    for condition in win_conditions:
        a, b, c = [boxes[i] for i in condition]
        if a.state == b.state == c.state != 0:
            a.color = b.color = c.color = RED
            message = f"Player {a.state} wins!"
            winner_found = True
            break

    if not winner_found and all(box.state != 0 for box in boxes):
        message = "It's a draw!"

    if reset_box.does_have_point():
        full_reset()
        message = ""

    return message


running = True
message = ""

while running:
    screen.fill(WHITE)

    for box in boxes:
        box.draw(screen)

    draw_reset_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            message = click()


    if message:
        message_surface = font.render(message, True, BLACK)
        screen.blit(message_surface, (70, 300))

    pygame.display.flip()

pygame.quit()

