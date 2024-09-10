from turtle import *
from random import randint
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ["black", "green", "yellow", "purple", "blue"]
randomCuerpo = random.randint(0, 4)
randomComida = random.randint(0, 4)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def inside_window(point):
    """Check if a point is inside the window boundaries."""
    return -200 < point.x < 190 and -200 < point.y < 190

def move_food():
    """Move food randomly one step at a time."""
    direction = randint(0, 3)
    directions = [vector(0, 100), vector(0, -100), vector(-100, 0), vector(100, 0)]
    new_food = food + directions[direction]
    if inside_window(new_food):
        food.move(directions[direction])

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    # Check for collision with boundaries or self
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()  # Move food randomly after being eaten
    else:
        snake.pop(0)

    clear()


    for body in snake:
        square(body.x, body.y, 9, color[randomCuerpo])

    square(food.x, food.y, 9, color[randomComida])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
