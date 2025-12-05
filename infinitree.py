#!/usr/bin/env python
import turtle as t
import random


def infinitree(branch_len, angle_var=25):
    if branch_len > 5:
        # color shift based on depth to look like an actual tree
        if branch_len > 40:
            t.color("saddlebrown")
            t.pensize(branch_len / 10)
        elif branch_len > 20:
            t.color("sienna")
            t.pensize(2)
        else:
            t.color("forestgreen")
            t.pensize(1)

        t.forward(branch_len)

        # right branch
        angle = random.uniform(15, angle_var)
        t.right(angle)
        infinitree(branch_len - random.uniform(10, 15), angle_var)

        # left branch
        t.left(angle * 2)
        infinitree(branch_len - random.uniform(10, 15), angle_var)

        t.right(angle)
        t.backward(branch_len)


t.speed(0)
t.left(90)
t.up()
t.backward(100)
t.down()
infinitree(75)
t.hideturtle()
t.mainloop()
