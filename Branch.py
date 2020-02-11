import turtle
from time import sleep

turtle.setup(800, 800)
turtle.speed("fastest")



def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)


for n in range(1, 6):
    turtle.clear()
    turtle.up()
    turtle.backward(200)
    turtle.down()
    draw(400, n)
    sleep(1)






turtle.exitonclick()
turtle.mainloop()



