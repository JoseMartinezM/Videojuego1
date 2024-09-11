from turtle import *
from random import randint
from freegames import square, vector
import random
import time

# Inicialización de la comida, la serpiente y otros parámetros
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)  # Dirección inicial de la serpiente
color = ["black", "green", "yellow", "purple", "blue", "orange", "pink", "cyan", "brown", "magenta"]  
speed = 100  # Velocidad inicial de la serpiente
food_speed = 2  # Velocidad de la comida
food_direction = vector(food_speed, 0)  # Dirección inicial de la comida
food_change_time = time.time()  # Tiempo para cambiar la dirección de la comida

def initialize_colors():
    "Selecciona colores aleatorios para la serpiente y la comida."
    global snake_color, food_color
    available_colors = color[:]
    snake_color = random.choice(available_colors)
    available_colors.remove(snake_color)
    food_color = random.choice(available_colors)

def change(x, y):
    "Cambia la dirección de la serpiente."
    aim.x = x
    aim.y = y

def inside(head):
    "Devuelve True si la cabeza de la serpiente está dentro de los límites."
    return -200 < head.x < 190 and -200 < head.y < 190

def inside_window(point):
    "Verifica si un punto está dentro de los límites de la ventana."
    return -200 < point.x < 190 and -200 < point.y < 190

def random_direction():
    "Genera una dirección aleatoria para la comida."
    directions = [vector(food_speed, 0), vector(-food_speed, 0), vector(0, food_speed), vector(0, -food_speed)]
    return random.choice(directions)

def move_food():
    "Mueve la comida a una nueva posición aleatoria y le asigna una nueva dirección."
    global food, food_direction
    food = vector(randint(-190, 180) // 10 * 10, randint(-190, 180) // 10 * 10)
    food_direction = random_direction()

def move():
    "Mueve la serpiente hacia adelante y gestiona el movimiento de la comida."
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
        move_food()  # Mueve la comida a una nueva posición
        speed = max(50, speed - 3)  # Aumenta la velocidad de la serpiente

    else:
        snake.pop(0)
    
    current_time = time.time()
    if current_time - food_change_time > 1:  # Cambia la dirección de la comida cada segundo
        food_direction = random_direction()
        food_change_time = current_time
    
    food.move(food_direction)
    if not inside_window(food):
        food_direction = random_direction()  # Cambia la dirección de la comida si sale de la ventana

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Dibuja el cuerpo de la serpiente

    square(food.x, food.y, 9, food_color)  # Dibuja la comida
    update()
    ontimer(move, speed)  # Llama a la función move nuevamente después de un intervalo basado en la velocidad

# Configuración inicial de la ventana del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
initialize_colors()  # Inicializa los colores de la serpiente y la comida
move()
done()
