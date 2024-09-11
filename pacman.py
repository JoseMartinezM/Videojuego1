from random import choice
from turtle import *

from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],

]

import random
from freegames import floor, vector

def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def generate_dynamic_map():
    tiles = [0] * 400

    for i in range(20):
        tiles[i] = 0  # Top border
        tiles[i + 380] = 0  # Bottom border
        tiles[i * 20] = 0  # Left border
        tiles[i * 20 + 19] = 0  # Right border

    for i in range(1, 19):
        for j in range(1, 19):
            if random.random() > 0.3:
                tiles[i * 20 + j] = 1
            else:
                tiles[i * 20 + j] = 0

    # Ensure Pacman's starting position is a path
    pacman_index = offset(pacman)
    tiles[pacman_index] = 1

    # Ensure ghost starting positions are paths
    for ghost in ghosts:
        ghost_index = offset(ghost[0])
        tiles[ghost_index] = 1

    return tiles

tiles = generate_dynamic_map()

def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()




def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for idx, (point, course) in enumerate(ghosts):
        if valid(point + course):
            point.move(course)
        else:
            # determina la velocidad de los fantasmas
            options = [
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            
            # Calcula la distancia entre pacman y el fantasma
            xDistance = pacman.x - point.x
            yDistance = pacman.y - point.y

            # Asigna la dirección dependiendo de la distancia (izquierda o derecha, arriba o abajo)
            xDirection = options[1] if xDistance < 0 else options[0]
            yDirection = options[3] if yDistance < 0 else options[2]

            # Determina si la dirección es horizontal o vertical dependiendo de cual
            # distancia es mayor
            horizontal = True if abs(xDistance) > abs(yDistance) else False

            # Intenta moverse en la direccion ideal hacia pacman,
            # pero siempre es posible que esto sea un movimiento invalido,
            # por lo que se tienen que checar los movimientos alternativos
            # que si sean validos. Se revisan en orden de que tan buenos
            # son los movimientos, para que asi el fantasma siempre se 
            # acerque a pacman
            if horizontal:
                if valid(point + xDirection):
                    plan = xDirection
                elif valid(point + yDirection):
                    plan = yDirection
                elif valid(point - xDirection):
                    plan = -xDirection
                else:
                    plan = -yDirection
            else:
                if valid(point + yDirection):
                    plan = yDirection
                elif valid(point + xDirection):
                    plan = xDirection
                elif valid(point - xDirection):
                    plan = -xDirection
                else:
                    plan = -yDirection

            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
