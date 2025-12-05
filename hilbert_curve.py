#!/usr/bin/env python
import turtle as t


def hilbert(level, angle, step):
    if level == 0:
        return
    t.right(angle)
    hilbert(level - 1, -angle, step)
    t.forward(step)
    t.left(angle)
    hilbert(level - 1, angle, step)
    t.forward(step)
    hilbert(level - 1, angle, step)
    t.left(angle)
    t.forward(step)
    hilbert(level - 1, -angle, step)
    t.right(angle)


t.speed(0)
t.penup()
t.goto(-200, 200)
t.pendown()
t.color("purple")
t.bgcolor("black")
hilbert(5, 90, 10)
t.hideturtle()
t.mainloop()
