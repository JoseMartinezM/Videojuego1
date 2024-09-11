from random import *
from turtle import *
from freegames import path

car = path('car.gif')
symbols = ['🍎', '🍌', '🍇', '🍓', '🍒', '🍍', '🥝', '🍉', '🥑', '🍆', '🥕', '🍋', '🍑', '🍅', '🍏', '🍈'] * 2
tiles = symbols
state = {'mark': None, 'taps': 0}  # Agregar contador de taps
hide = [True] * 64

def square(x, y):
    "Dibuja un cuadrado blanco con borde negro."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) al índice de las fichas."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte el número de fichas a coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y las fichas ocultas basado en el tap."
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # Incrementar contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Dibuja la imagen y las fichas."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar los cuadros
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Dibujar el número en la ficha marcada
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
	goto(x + 10, y + 5)
        color('black')
	write(tiles[mark], font=('Arial', 20, 'normal'), align="center")
	
    # Mostrar el contador de taps
    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 20, 'normal'))

    # Verificar si se han destapado todas las fichas
    if all(not hidden for hidden in hide):
        goto(-150, 0)
        write('¡Felicidades! Has destapado todos los cuadros.', font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
