#!/usr/bin/env python
import turtle as t
import math


def draw_kite(size):
    t.begin_fill()
    t.forward(size)
    t.left(72)
    t.forward(size)
    t.left(144)
    t.forward(size)
    t.left(72)
    t.forward(size)
    t.left(72)
    t.end_fill()


def penrose_sun(size, depth):
    colors = ["#FF6B9D", "#C44569", "#FFA07A", "#FFD93D", "#6BCB77"]
    for i in range(10):
        t.color(colors[i % len(colors)])
        t.fillcolor(colors[(i + 1) % len(colors)])
        draw_kite(size)
        t.right(36)
        if depth > 0 and i % 2 == 0:
            t.forward(size * 0.6)
            penrose_sun(size * 0.4, depth - 1)
            t.backward(size * 0.6)


t.speed(0)
t.bgcolor("black")
penrose_sun(100, 2)
t.hideturtle()
t.mainloop()
