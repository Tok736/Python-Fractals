from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)
bgcolor("#000000")

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

def minkowski(l, n):
    move(-l / 2, -l / 4)
    rotates = [45, -90, 45]
    k = 2/sqrt(2)
    draw(rotates, k, l, n)

l = 500
for n in range(1, 18):
    reset()
    color("#d3fdfe")
    hideturtle()
    tracer(0)
    minkowski(l, n)
    update()
    sleep(0.5)


exitonclick()
mainloop()



