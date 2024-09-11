from turtle import *
from random import randint
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ["black", "green", "yellow", "purple", "blue"]
speed = 100  
randomCuerpo = random.randint(0, 4)
randomComida = random.randint(0, 4)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def random_position():
    """Generate a random position for the food within the boundaries."""
    x = randint(-190, 180) // 10 * 10
    y = randint(-190, 180) // 10 * 10
    return vector(x, y)

def move_food():
    """Move food to a new random position."""
    global food
    food = random_position()

def move():
    """Move snake forward one segment."""
    global speed
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake length:', len(snake))
        move_food()  
        speed = max(50, speed - 3)  
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color[randomCuerpo])

    square(food.x, food.y, 9, color[randomComida])
    update()
    ontimer(move, speed)  

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

