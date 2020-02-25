from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(l, n):
    if n == 0:
        left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        forward(x)
        left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        right(135)
    up()
    forward(x)
    left(180)
    forward(l)
    down()


def branch(l, n):
    move(-l/2, 0)
    draw(l, n)

l = 800
for n in range(1, 8):
    reset()
    hideturtle()
    tracer(0)
    branch(l, n)
    update()
    sleep(1)




exitonclick()
mainloop()



