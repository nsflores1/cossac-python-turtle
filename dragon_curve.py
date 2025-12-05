#!/usr/bin/env python
import turtle as t


def dragon_curve(order, length):
    if order == 0:
        t.forward(length)
    else:
        dragon_curve(order - 1, length)
        t.left(90)
        dragon_curve_reversed(order - 1, length)


def dragon_curve_reversed(order, length):
    if order == 0:
        t.forward(length)
    else:
        dragon_curve(order - 1, length)
        t.right(90)
        dragon_curve_reversed(order - 1, length)


t.speed(0)
t.pensize(1)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.bgcolor("black")

for i in range(12):
    t.color(colors[i % len(colors)])
    dragon_curve(i, 10)
    t.right(90)

t.hideturtle()
t.mainloop()
