from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
"""List of emojis instead of symbols"""
symbols = ['🍎', '🍏', '🍊', '🍋', '🍉', '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥭', '🥥', '🥝', '🍅', '🥕', '🥦', '🥒', '🌽', '🥔', '🍠', '🍆', '🌶', '🌰', '🧄', '🧅', '🧈', '🍯', '🧂', '🧃', '🍹', '🍺', '🍻', '🍷', '🍸', '🍶', '🍵', '🍶', '🥃', '🧉', '🧊', '🧋']
tiles = symbols * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Contador de taps

def square(x, y):
    """Draw white square with black outline at (x, y)."""
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
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Necesario para modificar la variable global
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    tap_count += 1  # Incrementar el contador cada vez que se hace un tap
    
def revealed():
    return all(not h for h in hide)

def draw():
    """Draw image and tiles."""
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
        write(tiles[mark],align="center",font=('Arial', 30, 'normal'))

    # Dibujar el contador en la esquina superior izquierda
    up()
    goto(-200, 200)
    color('black')
    write(f"Contador de tabs: {tap_count}", align="left", font=("Arial", 12, "normal"))

    if revealed():
        up()
        goto(-200, -250)
        write("Felicidades has ganado, has destapado todo", align="left", font=("Arial", 14, "bold"))
        
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 550, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
