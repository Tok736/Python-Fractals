from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)
bgcolor("#000000")

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(f, k, l, n):
    if n == 1:
        left(f * 90)
        for i in range(3):
            right(f * 90)
            forward(l)
        return
    d = l / k ** (n - 1)
    right(f * 90)
    draw(-f, k, l / k, n - 1)
    right(f * 90)
    forward(d)
    draw(f, k, l / k, n - 1)
    left(f * 90)
    forward(d)
    left(f * 90)
    draw(f, k, l / k, n - 1)
    forward(d)
    right(f * 90)
    draw(-f, k, l / k, n - 1)
    right(f * 90)


def peanoCurve(l, n):
    d = l - l*(1/2) ** n
    move(-d, -d)
    setheading(90)
    k = 2
    draw(1, k, l, n)

l = 380
for n in range(1, 9):
    reset()
    color("#d3fdfe")
    hideturtle()
    tracer(0)
    peanoCurve(l, n)
    update()
    sleep(1)


exitonclick()
mainloop()



