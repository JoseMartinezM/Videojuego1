"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector
from math import sqrt

def line(start, end):
    "Dibuja una línea desde el punto de inicio hasta el punto final."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Dibuja un cuadrado desde el punto de inicio hasta el punto final."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def draw_circle(start, end):
    "Dibuja un círculo utilizando el punto de inicio como centro y la distancia como radio."
    up()
    goto(start.x, start.y)
    down()
    
    radius = sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)  # Calcula el radio

    begin_fill()
    circle(radius)  # Usa el método circle del módulo turtle
    end_fill()

def rectangle(start, end):
    "Dibuja un rectángulo desde el punto de inicio hasta el punto final."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()

def triangle(start, end):
    "Dibuja un triángulo equilátero desde el punto de inicio."
    up()
    goto(start.x, start.y)
    down()
    
    begin_fill()

    side_length = sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)  # Calcula la longitud del lado

    for _ in range(3):
        forward(side_length)
        left(120)  # 120 grados para el triángulo equilátero

    end_fill()

def tap(x, y):
    "Almacena el punto inicial o dibuja la forma seleccionada."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Almacena el valor de la forma seleccionada en el estado."
    state[key] = value

# Configuración inicial del estado y pantalla
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')  # Añadir el color morado con P
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')  # Usa draw_circle en lugar de circle
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
