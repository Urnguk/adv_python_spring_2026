import turtle
from functools import cache

@cache
def dragon_angles(n):
    if n == 0:
        return []
    prev = dragon_angles(n - 1)
    return prev + [True] + [not(x) for x in prev[::-1]]

def draw_dragon(t, n, step_dist):
    angles = dragon_angles(n)
    t.fd(step_dist)
    for i in range(len(angles)):
        if angles[i]:
            t.rt(90)
        else:
            t.lt(90)
        t.fd(step_dist)




def triangle(t, dist, n):
    if n == -1:
        return
    for i in range(3): 
        triangle(t, dist / 2, n - 1)
        t.fd(dist)
        t.rt(120)


d = 300
turtle.tracer(0)
t = turtle.Turtle()
draw_dragon(t, 5, 20)
turtle.update()
turtle.done()
