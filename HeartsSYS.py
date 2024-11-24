import turtle
from math import pi, sin, cos

def draw_heart(w, h, color, start_pos):
    t.pensize(2.5)
    t.up()
    t.goto(start_pos) 
    t.down()
    t.fillcolor(color)
    t.begin_fill()

  a = 0
    points = []
    while a < 2 * pi:
        x = w * (16 * sin(a) ** 3) + start_pos[0]
        y = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a)) + start_pos[1]
        points.append((x, y))
        if len(points) == 1:
            t.up()
            t.goto(points[0])  # Move to the starting point
            t.down()
        else:
            t.goto(x, y)
        a += 0.01
    t.goto(points[0])  # Close the shape
    t.end_fill()
