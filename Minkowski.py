from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(rotates, k, l, n):
    if n == 1:
        forward(l)
        return

    draw(rotates, k, l / k, n - 1)
    for rot in rotates:
        left(rot)
        draw(rotates, k, l / k, n - 1)

def minkowski(l, n):
    move(-l / 2, 0)
    rotates = [90, -90, -90, 0, 90, 90, -90]
    k = 4
    draw(rotates, k, l, n)

l = 900
for n in range(1, 7):
    reset()
    hideturtle()
    tracer(0)
    minkowski(l, n)
    update()
    sleep(1)


exitonclick()
mainloop()



