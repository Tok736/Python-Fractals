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

    left(rotates[0])
    for rot in rotates[1:]:
        draw(rotates, k, l / k, n - 1)
        left(rot)

def curve(l, n):
    rotates = [45, -90, 0, 90, -45]
    k = 4 / sqrt(2)
    draw(rotates, k, l, n)

def island(l, n):
    move(-l / 2, l / 2)
    for i in range(4):
        curve(l, n)
        right(90)

l = 480
for n in range(1, 9):
    reset()
    hideturtle()
    tracer(0)
    island(l, n)
    update()
    sleep(1)


exitonclick()
mainloop()



