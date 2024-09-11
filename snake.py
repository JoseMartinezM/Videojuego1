from turtle import *
from random import randint
from freegames import square, vector
import random
import time

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ["black", "green", "yellow", "purple", "blue", "orange", "pink", "cyan", "brown", "magenta"]
speed = 100  
food_speed = 2  
randomCuerpo = random.randint(0, 4)
randomComida = random.randint(0, 4)
food_direction = vector(food_speed, 0)  
food_change_time = time.time()  

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

def random_direction():
    """Generate a random direction for the food."""
    directions = [vector(food_speed, 0), vector(-food_speed, 0), vector(0, food_speed), vector(0, -food_speed)]
    return random.choice(directions)

def move_food():
    """Move food to a new random position and direction."""
    global food, food_direction
    food = vector(randint(-190, 180) // 10 * 10, randint(-190, 180) // 10 * 10)
    food_direction = random_direction()

def move():
    """Move snake forward one segment."""
    global speed, food_direction, food_change_time
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
    current_time = time.time()
    if current_time - food_change_time > 1:  
        food_direction = random_direction()
        food_change_time = current_time
    
    food.move(food_direction)
    if not inside_window(food):
        food_direction = random_direction()  

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
