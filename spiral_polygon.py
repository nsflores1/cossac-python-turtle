#!/usr/bin/env python
import turtle as t


def spiral_polygon(sides, size, angle_shift, iterations):
    for i in range(iterations):
        t.color((i / iterations, 0.5, 1 - i / iterations))
        for _ in range(sides):
            t.forward(size)
            t.left(360 / sides)
        t.left(angle_shift)
        size *= 0.95


t.speed(0)
t.bgcolor("black")
t.pensize(2)
spiral_polygon(6, 100, 5, 80)
t.hideturtle()
t.mainloop()
