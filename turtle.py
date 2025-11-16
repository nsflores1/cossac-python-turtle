#!/usr/bin/env python
import turtle as t

# this makes a pretty star!
t.color("red")
t.fillcolor("yellow")
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.mainloop()
