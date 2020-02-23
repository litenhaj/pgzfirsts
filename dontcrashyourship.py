from random import randint

WIDTH = 800
HEIGHT = 600

starship = Actor("balloon")
starship.pos = 400, 300

sentinel = Actor("bird-up")
sentinel.pos = 400, 300

station = Actor("house")
station.pos = randint(800, 1600), 460

asteorid = Actor("tree")
asteorid.pos = randint(800, 1600), 450

sentinel_upp = True
upp = False
spelet_slut = False
summa = 0
antal_uppdateringar = 0

summor = []

def uppdatera_rekord():
    global summa, summor
    filnamn = r"./rekord.txt"
    summor = []
    with open(filnamn, "r") as fil:
        rad = fil.readline()
        rekorden = rad.split()
        for rekord in rekorden:
            if(summa > int(rekord)):
                summor.append(str(summa) + " ")
                summa = int(rekord)
            else:
                summor.append(str(rekord) + " ")
        with open(filnamn, "w") as fil:
            for rekord in summor:
                fil.write(rekord)

def visa_rekord():
    screen.draw.text("REKORD", (350, 150), color="black")
    Y = 175
    position = 1
    for rekord in summor:
        screen.draw.text(str(position) + ". " + rekord, (350, y), color="black")
        y += 25
        position += 1

def draw():
    screen.blit("background", (0, 0))
    if not spelet_slut:
        starship.draw()
        sentinel.draw()
        station.draw()
        asteorid.draw()
        screen.draw.text("Summa: " + str (summa), (700, 5), color="black")
    else:
        visa_rekord()

def on_mouse_down():
    global upp
    upp = True
    starship.y -= 50

def on_mouse_up():
    global upp
    upp = False

def flaxa():
    global sentinel_upp
    if sentinel_upp:
        sentinel.image = "bird-up"
        sentinel_upp = True

def update():
    global spelet_slut, summa, antal_uppdateringar
    if not upp:
        starship.y += 1

    if sentinel.x > 0:
        sentinel.x -= 4
        if antal_uppdateringar == 9:
            flaxa()
            antal_uppdateringar = 0
        else:
            antal_uppdateringar += 1
    else:
        sentinel.x = randint(800, 1600)
        sentinel.y = randint(10, 200)
        summa += 1
        antal_uppdateringar = 0

    if station.right > 0:
        station.x -= 2
    else:
        station.x = randint(800, 1600)
        summa += 1

    if asteorid.right > 0:
        asteorid.x -= 2
    else:
        asteorid.x = randint(800, 1600)
        summa += 1

    if starship.top < 0 or starship.bottom > 560:
        spelet_slut = True
        uppdatera_rekord()

    if starship.collidepoint(sentinel.x, sentinel.y) or \
       starship.collidepoint(station.x, station.y) or \
       starship.collidepoint(asteorid.x, asteorid.y):
        spelet_slut = True
        uppdatera_rekord()
