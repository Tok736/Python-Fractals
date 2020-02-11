from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def draw(k, l, n):
    if (n == 0): return
    forward(l)
    left(45)
    draw(k, l / k, n - 1)
    right(90)
    draw(k, l / k, n - 1)
    right(135)
    forward(l)
    right(180)

def tree(l, n):
    move(0, -1.5 * l)
    setheading(90)
    k = 1.5
    draw(k, l, n)

l = 250
for n in range(1, 10):
    reset()
    hideturtle()
    tracer(0)
    tree(l, n)
    update()
    sleep(1)



exitonclick()
mainloop()



