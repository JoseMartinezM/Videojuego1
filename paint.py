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
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end): #Funcion para añadir un cuadrado con s
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end): #Funcion para añadir un circulo con c
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    
    width = sqrt((end.x - start.x)**2) + ((end.y - start.y)**2)

    begin_fill()


    for count in range(360):
        forward(width/360)
        left(1)

    end_fill()

    pass  # TODO


def rectangle(start, end): # Funbcion para un rectangulo
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
        
    end_fill()

    pass  # TODO


def triangle(start, end): #Funcion para triangulo
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    
    begin_fill()

    forward(end.x - start.x)
    left(90)
    forward(end.x - start.x)
    left(135)
    forward(end.x - start.x)

    end_fill()

    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


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
onkey(lambda: color('purple'),'P') #Añadir el color morado con P
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
