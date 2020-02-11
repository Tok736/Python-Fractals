from turtle import *
from math import sqrt
from time import sleep

setup(1.0, 1.0)

def move(x, y):
    up()
    goto(x, y)
    down()

def lSystem(start, rules):
    newStart = []
    for letter in start:
        for rule in rules:
            if letter == rule[0]:
                newStart.append(rule[1])
                break
    start = "".join(newStart)
    return start

def draw(op, measure):
    if op == "fd":
        forward(measure)
    elif op == "l":
        left(measure)
    elif op == "r":
        right(measure)

def drawer(command, ops):
    for letter in command:
        for op in ops:
            if op[0] == letter:
                draw(op[1], op[2])
                break

def dragonCurve(l, n):
    move(-l / 4, l / 4)
    setheading(- (n % 8) * 45)
    k = sqrt(2)
    l = l / (k ** (n - 1))
    start = "FX" 
    rules = [
    ("X", "X+YF+"),
    ("Y", "-FX-Y"),
    ("F", "F"),
    ("-", "-"),
    ("+", "+")
    ]
    ops = [
    ("X", "none", l),
    ("Y", "none", l),
    ("F", "fd", l),
    ("+", "l", 90),
    ("-", "r", 90)
    ]
    for i in range(n - 1):
        start = lSystem(start, rules)
    drawer(start, ops)

l = 500
for n in range(1, 19):
    reset()
    hideturtle()
    tracer(0)
    dragonCurve(l, n)
    update()
    sleep(0.5)


exitonclick()
mainloop()



