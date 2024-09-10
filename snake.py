from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["black", "green", "yellow", "purple", "blue"]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food to a random position within boundaries."""
    while True:
        new_x = randrange(-19, 19) * 10
        new_y = randrange(-19, 19) * 10
        new_food = vector(new_x, new_y)
        if new_food not in snake:
            food.x = new_food.x
            food.y = new_food.y
            break

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()  # Mueve la comida a una nueva posición
        randomComida = random.randint(0, 4)  # Cambia el color de la comida
    else:
        snake.pop(0)

    clear()

    # Elige un color aleatorio para cada segmento del cuerpo de la serpiente
    for body in snake:
        randomCuerpo = random.randint(0, 4)  # Cambia el color del cuerpo en cada iteración
        square(body.x, body.y, 9, colors[randomCuerpo])

    # Dibuja la comida con un color aleatorio
    square(food.x, food.y, 9, colors[randomComida])
    update()

    # Llama a move() de nuevo después de 100ms
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
