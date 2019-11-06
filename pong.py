# Simple Ping_Pong in Python 3
import turtle
import os

# plansza gry
okno = turtle.Screen()
okno.title("Ping_pong :D")
okno.bgcolor("black")
okno.setup(width=1600, height=1000)
okno.tracer(0)

# wyniki
wynik_a = 0
wynik_b = 0

# deska gracz 1
deska_a = turtle.Turtle()
deska_a.speed(0)
deska_a.shape("square")
deska_a.color("silver")
deska_a.shapesize(stretch_wid=7, stretch_len=1.5)
deska_a.penup()
deska_a.goto(-750, 0)

# deska gracz 2
deska_b = turtle.Turtle()
deska_b.speed(0)
deska_b.shape("square")
deska_b.color("silver")
deska_b.shapesize(stretch_wid=7, stretch_len=1.5)
deska_b.penup()
deska_b.goto(750, 0)

# piłka do gry
pilka = turtle.Turtle()
pilka.speed(0)
pilka.shape("circle")
pilka.color("purple")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 1/5
pilka.dy = -1/5


# tablica tabów
tab = turtle.Turtle()
tab.speed(0)
tab.color("gold")
tab.penup()
tab.hideturtle()
tab.goto(0,425)
tab.write("Player A: 0  Player B:0", align="center", \
            font=("Comic Sans MS", 36, "bold"))


# poruszanie się deskami
def deska_a_up():
    y = deska_a.ycor()
    y += 50
    deska_a.sety(y)

def deska_a_down():
    y = deska_a.ycor()
    y -= 50
    deska_a.sety(y)


def deska_b_up():
    y = deska_b.ycor()
    y += 50
    deska_b.sety(y)

def deska_b_down():
    y = deska_b.ycor()
    y -= 50
    deska_b.sety(y)


# sterowanie
okno.listen()
okno.onkeypress(deska_a_up, "w")
okno.onkeypress(deska_a_down, "s")
okno.onkeypress(deska_b_up, "Up")
okno.onkeypress(deska_b_down, "Down")


while True:
    okno.update()
# poruszanie się piłki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)
# granice planszy i dodawanie punktów
    if pilka.ycor() > 490:
        pilka.sety(490)
        pilka.dy *= -1
        os.system("aplay wall.wav&")

    if pilka.ycor() < -490:
        pilka.sety(-490)
        pilka.dy *= -1
        os.system("aplay wall.wav&")

    if pilka.xcor() > 790:
        pilka.goto(0, 0)
        pilka.dx *= -1
        wynik_a += 1
        tab.clear()
        tab.write("Player A: {}  Player B: {}".format(wynik_a, wynik_b),\
                    align="center", font=("Comic Sans MS", 36, "bold"))
        os.system("aplay bounce.wav&")

    if pilka.xcor() < -790:
        pilka.goto(0, 0)
        pilka.dx *= -1
        wynik_b += 1
        tab.clear()
        tab.write("Player A: {}  Player B: {}".format(wynik_a, wynik_b),\
                    align="center", font=("Comic Sans MS", 36, "bold"))
        os.system("aplay bounce.wav&")

# dobijanie piłki przez deski
    if (pilka.xcor() > 740 and pilka.xcor() < 750) and (pilka.ycor() \
        < deska_b.ycor() + 65 and pilka.ycor() > deska_b.ycor() -65):
        pilka.setx(740)
        pilka.dx *= -1
        os.system("aplay pong.wav&")

    if (pilka.xcor() < -740 and pilka.xcor() > -750) and (pilka.ycor() \
        < deska_a.ycor() + 65 and pilka.ycor() > deska_a.ycor() -65):
        pilka.setx(-740)
        pilka.dx *= -1
        os.system("aplay pong.wav&")
