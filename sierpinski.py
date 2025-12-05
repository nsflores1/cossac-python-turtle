#!/usr/bin/env python
import turtle as t


def sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(length / 2, depth - 1)
        t.forward(length / 2)
        sierpinski(length / 2, depth - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski(length / 2, depth - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)


t.speed(0)
t.penup()
t.goto(-200, -150)
t.pendown()
t.color("purple")
sierpinski(400, 5)
t.hideturtle()
t.mainloop()
