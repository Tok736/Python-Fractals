from random import gauss
from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)
bgcolor("#000000")

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(k, l, n):
    if (n == 0): return
    lAngle = 10 * gauss(0, 1) + 10
    rAngle = 10 * gauss(0, 1)
    addingLen = l * gauss(0, 0.05)
    addingK = l * gauss(0, 0.02)
    forward(l + addingLen)
    left(45 + lAngle)
    draw(k, addingK + l / k, n - 1)
    right(90 + lAngle + rAngle)
    draw(k, addingK + l / k, n - 1)
    right(135 - rAngle)
    forward(l + addingLen)
    right(180)

def tree(l, n):
    move(0, -1.5 * l)
    setheading(90)
    k = 1.6 + gauss(0, 0.05)
    draw(k, l, n)

l = 250
n = 9
for i in range(100):
    reset()
    color("#d3fdfe")
    hideturtle()
    tracer(0)
    tree(l, n)
    update()
    sleep(2)



exitonclick()
mainloop()

