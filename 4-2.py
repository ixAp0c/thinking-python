import turtle
import math

# Write an appropriately general set of functions that can draw flowers as in
# Figure 4.1

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def draw_arc(t, r, angle):
    """ Draws an arc with the given radius(r) and angle 
    """
    arc_length = 2 * math.pi * r * (abs(angle) / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)

def draw_petal(t, r, angle):
    turn_angle = 180 - angle
    draw_arc(t, r, angle)
    bob.lt(turn_angle)
    draw_arc(t, r, angle)
    bob.lt(turn_angle)

def draw_flower(t, r, angle, sides):
    n = 360 / sides
    for i in range(sides):
        draw_petal(t, r, angle)
        t.lt(n)

def move(t, distance):
    t.pu()
    t.fd(distance)
    t.pd()

bob = turtle.Turtle()

move(bob, -170)
draw_flower(t=bob, r=80, angle=45, sides=7)
move(bob, 170)
draw_flower(t=bob, r=80, angle=55, sides=10)
move(bob, 170)
draw_flower(t=bob, r=80, angle=35, sides=20)

turtle.mainloop()
