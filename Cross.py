from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def square(l, clr="black"):
    color(clr)
    begin_fill()
    for i in range(4):
        forward(l)
        right(90)
    end_fill()   

def draw(empty, rec, k, l, n):
    if (n == 0): return

    x = xcor()
    y = ycor()
    for pos in empty:
        goto(x + l * pos[0], y - l * pos[1])
        square(l, "white")
    for pos in rec:
        goto(x + l * pos[0], y - l * pos[1])
        draw(empty, rec, k, l / k, n - 1)
    goto(x, y)


def cross(l, n):
    up()
    goto(-l / 2, l / 2)
    square(l, "black")
    empty = [(0, 0), (2, 0), (0, 2), (2, 2)]
    rec = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    k = 3
    draw(empty, rec, k, l / 3, n - 1)

l = 700
for n in range(1, 7):
    reset()
    hideturtle()
    tracer(0)
    cross(l, n)
    update()
    sleep(1)



exitonclick()
mainloop()



