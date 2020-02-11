from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(factor, rotates, k, l, n):
    if n == 1:
        forward(l)
        return
    f = factor
    left(factor * rotates[0])
    for rot in rotates[1:]:
        f *= -1
        draw(f, rotates, k, l / k, n - 1)
        left(factor * rot)

def sierpinski(l, n):
    move(-l / 2, -sqrt(3) / 4 * l)
    rotates = [60, -60, -60, 60]
    k = 2
    draw(1, rotates, k, l, n)


l = 700
for n in range(1, 12):
    reset()
    hideturtle()
    tracer(0)
    sierpinski(l, n)
    update()
    sleep(1)


exitonclick()
mainloop()



