from random import gauss
from turtle import *
from math import sqrt
from time import sleep







def isInSet(x, y, maxIter=256):
    z = complex(0, 0)
    C = complex(x, y)
    iters = 0
    for i in range(maxIter):
        iters += 1
        z = z ** 2 + C
        if (z.real ** 2 + z.imag ** 2 >= 4): break
    print(iters)
    if iters >= maxIter: return -1
    else: return iters


def dotxy(x, y, r):
    goto(x, y)
    dot(r)

setup(1.0, 1.0)
bgcolor("#450577")
up()
hideturtle()
tracer(0)

for x in range(-250, 250):
    for y in range(0, 250):
        iters = -1
        # iters = isInSet(x * 0.008, y * 0.008)
        if iters == - 1:
            color("#000000")
            dotxy(x, y, 2)
            dotxy(x, -y, 2)
        else:
            c = (str(hex(iters))[2:]).upper()
            if len(c) == 1: c += "0"
            color("#45" + c + "77")
            dotxy(x, y, 2)
            dotxy(x, -y, 2)
    update()








# for i in range(100):
#     reset()
#     color("#d3fdfe")
#     hideturtle()
#     tracer(0)
#     tree(l, n)
#     update()
#     sleep(2)



mainloop()









