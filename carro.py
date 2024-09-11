from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
"""Lista de emojis en lugar de símbolos"""
symbols = ['🍎', '🍏', '🍊', '🍋', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥭', '🥥', '🥝', '🍅', '🥕', '🥦', '🥒', '🌽', '🥔', '🍠', '🍆', '🌶', '🌰', '🧄', '🧅', '🧈', '🍯', '🧂', '🧃', '🍹', '🍺', '🍻', '🍷', '🍸', '🍶', '🍵', '🍶', '🥃', '🧉', '🧊', '🧋']
tiles = symbols * 2  # Duplicar los emojis para que haya pares
state = {'mark': None}
hide = [True] * 64  # Mantener ocultos los cuadros
tap_count = 0  # Contador de taps

def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en las coordenadas (x, y)."""
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
    """Convierte las coordenadas (x, y) en el índice correspondiente en las fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte el número de la ficha en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza la marca y las fichas ocultas según el clic del usuario."""
    global tap_count  # Se necesita para modificar la variable global tap_count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    tap_count += 1  # Incrementar el contador cada vez que se hace un clic (tap)

def revealed():
    """Devuelve True si todas las fichas están destapadas."""
    return all(not h for h in hide)

def draw():
    """Dibuja la imagen y las fichas en la pantalla."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 10)
        color('black')
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    # Dibujar el contador de taps en la esquina superior izquierda
    up()
    goto(-200, 200)
    color('black')
    write(f"Contador de taps: {tap_count}", align="left", font=("Arial", 12, "normal"))

    # Si todas las fichas están reveladas, mostrar un mensaje de victoria
    if revealed():
        up()
        goto(-200, -250)
        write("¡Felicidades! Has ganado, has destapado todo", align="left", font=("Arial", 14, "bold"))
        
    update()
    ontimer(draw, 100)  # Actualizar la pantalla cada 100 milisegundos

# Mezclar las fichas antes de comenzar
shuffle(tiles)
setup(420, 550, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
