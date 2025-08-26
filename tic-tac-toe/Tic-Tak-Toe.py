
import turtle

t = turtle.Turtle()
t.speed(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("blue")

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
        self.color = "black"

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.pencolor(self.color)
        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)

        if self.state == 1:
            t.penup()
            t.goto(self.x + 15, self.y - 40)
            t.pendown()
            t.write("X", font=("Arial", 24, "normal"))
        elif self.state == 2:
            t.penup()
            t.goto(self.x + 15, self.y - 40)
            t.pendown()
            t.write("O", font=("Arial", 24, "normal"))
        t.penup()

    def does_have_point(self, x, y):
        return (self.x <= x <= self.x + self.width) and (self.y - self.height <= y <= self.y)

boxes = []
index = 0
for x in range(0, 150, 50):
    for y in range(0, 150, 50):
        box = Box(x, y, 50, 50, index)
        boxes.append(box)
        index += 1

for box in boxes:
    box.draw()

reset_box = Box(50, -80, 40, 100, -1)
reset_box.color = "black"

def on_click(x, y):
    for box in boxes:
        if box.does_have_point(x, y):
            if box.state == 0:
                count = sum(1 for b in boxes if b.state != 0)
                box.state = 1 if count % 2 == 0 else 2
                box.draw()
                break


    winner_found = False
    for condition in win_conditions:      
        a, b, c = [boxes[i] for i in condition]
        if a.state == b.state == c.state != 0:
            def find_winner():
                pen.clear()
                pen.goto(75, -20)
                pen.write(f"Player {a.state} wins!", align="center", font=("Arial", 24, "bold"))
                pen.goto(-100, -50)
                a.color = "red"
                b.color = "red"
                c.color = "red"
                a.draw()
                b.draw()
                c.draw()
                reset_box.draw()
                t.penup()
                t.goto(reset_box.x + reset_box.width/2, reset_box.y - reset_box.height + 5)
                t.pendown()
                t.pencolor("black")
                t.write("RESET", align="center", font=("Arial", 18, "bold"))
                t.penup()
                winner_found = True
            find_winner()

    if not winner_found and all(box.state != 0 for box in boxes):
        pen.goto(0, -100)
        pen.write("It's a draw!", align="center", font=("Arial", 24, "bold"))

    if reset_box.does_have_point(x, y):
        full_reset()

def full_reset():
    for temp_t in turtle.Screen().turtles():
        temp_t.clear()
    pen.clear()
    for box in boxes:
        box.state = 0
        box.color = "black"
        box.draw()
    t.penup()
    t.goto(reset_box.x + reset_box.width/2, reset_box.y - reset_box.height + 5)
    t.pendown()
    t.pencolor("black")
    t.write("RESET", align="center", font=("Arial", 18, "bold"))
    t.penup()

t.hideturtle()
turtle.onscreenclick(on_click)
turtle.done()
