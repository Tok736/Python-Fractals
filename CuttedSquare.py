from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)
bgcolor("#000000")
 


def move(x, y):
    up()
    goto(x, y)
    down()

def getK(func, rotates):
    up()
    l = 100
    startx = xcor()
    draw(rotates, 1, l, 1)
    x1 = xcor()
    goto(0, 0)
    draw(rotates, 1, l, 2)
    x2 = xcor()
    k = (x2 - startx) / (x1 - startx)
    print(x1, x2, startx)
    goto(0, 0)
    down()
    return abs(k)

def draw(rotates, k, l, n):
    if n == 1:
        forward(l)
        return

    left(rotates[0])
    for rot in rotates[1:]:
        draw(rotates, k, l / k, n - 1)
        left(rot)

def cuttingSquare(l, n, theta = 45):
    rotates = [0, theta, -2 * theta, theta, 0]
    k = getK(draw, rotates)
    print(k)
    move(-l / 2, 0)
    draw(rotates, k, l, n)
    right(180)
    draw(rotates, k, l, n)

l = 500
n = 5
for theta in range(-90, 91):
    reset()
    color("#d3fdfe")
    hideturtle()
    tracer(0)
    cuttingSquare(l, n, theta)
    update()
    sleep(0.01)


exitonclick()
mainloop()



