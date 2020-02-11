from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(rotates, lens, k, l, n):
    

    left(rotates[0])
    for i in range(1, len(rotates)):
        if n == 1: forward(l * lens[i - 1])
        else: draw(rotates, lens, k, lens[i - 1] * l / k, n - 1)
        left(rotates[i])

    if n == 1:
        return


def curve(l, n):
    rotates = [0, 120, 180, 120, 180, 120, 0]
    lk = 1 / 2
    lens = [1, lk, lk, lk, lk, 1]
    k = 2
    draw(rotates, lens, k, l, n)

def iceCurve(l, n):
    move(-l, 0)
    curve(l, n)

l = 400
for n in range(1, 7):
    reset()
    hideturtle()
    tracer(0)
    iceCurve(l, n)
    update()
    sleep(1)


exitonclick()
mainloop()



