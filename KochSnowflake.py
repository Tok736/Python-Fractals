from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)
bgcolor("#000000")

def move(x, y):
    up()
    goto(x, y)
    down()


def draw(l, n):
    if n == 1:
        forward(l)
        return

    draw(l / 3, n - 1)
    left(60)
    draw(l / 3, n - 1)
    right(120)
    draw(l / 3, n - 1)
    left(60)
    draw(l / 3, n - 1)


def koch(l, n):
    up()
    goto(- l / 2, 0)
    down()
    draw(l, n)

def snowflake(l, n):
    up()
    goto(- l / 2, l * sqrt(3) / 6)
    down()
    for i in range(3):
        draw(l, n)
        right(120)

l = 550
for n in range(1, 7):
    reset()
    hideturtle()
    tracer(0)
    color("#d3fdfe")
    snowflake(l, n)
    update()
    sleep(1)

exitonclick()
mainloop()



