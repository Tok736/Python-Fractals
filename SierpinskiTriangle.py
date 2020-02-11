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

def sierpinskiTriangle(l, n):
    move(-l/2, l * sqrt(3) / 4)
    setheading(0)
    k = 2
    l = l / (k ** (n - 1))
    start = "F-G-G" 
    rules = [
    ("F", "F-G+F+G-F"),
    ("G", "GG"),
    ("-", "-"),
    ("+", "+")
    ]
    ops = [
    ("G", "fd", l),
    ("F", "fd", l),
    ("+", "l", 120),
    ("-", "r", 120)
    ]
    for i in range(n - 1):
        start = lSystem(start, rules)
    drawer(start, ops)

l = 700
for n in range(1, 10):
    reset()
    hideturtle()
    tracer(0)
    sierpinskiTriangle(l, n)
    update()
    sleep(1)

exitonclick()
mainloop()



