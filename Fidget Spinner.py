from turtle import *
from random import randint
sr = Screen()
sr.title("Fidget Spinner")
sr.bgcolor("Sky Blue")
sr.colormode(255)
turn = 0
def spinner():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    clear()
    angle = turn/10
    left(angle)
    # print("Spinner")
    forward(100)
    dot(120,r,g,b)
    back(100)
    left(120)
    forward(100)
    dot(120,r,g,b)
    back(100)
    left(120)
    forward(100)
    dot(120,r,g,b)
    back(100)
    left(120)
    update()
def animate():
    global turn
    if turn > 0:
        turn = turn -1
    spinner()
    ontimer(animate,20)
def flick():
    global turn
    turn = turn +10
    print(turn)
tracer(False)
width(20)
onkey(flick,"space")
listen()
animate()
done()
