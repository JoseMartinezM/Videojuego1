from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Responde al clic en la pantalla, reposiciona la bola y ajusta su velocidad."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 20  
        speed.y = (y + 200) / 20

def inside(xy):
    "Devuelve True si las coordenadas están dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibuja la bola y los objetivos en la pantalla."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Mueve la bola y los objetivos en la pantalla."
    global target_speed  

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= target_speed

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            if not inside(target):
                target.x = 200
                target.y = randrange(-150, 150)
            targets.append(target)

    draw()

    target_speed += 0.01  # Aumenta gradualmente la velocidad de los objetivos

    ontimer(move, 50)

target_speed = 0.5  # Velocidad inicial de los objetivos

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
