from vpython import *

ball1 = sphere(pos=vector(-5, 0, 0), radius=0.5, color=color.red)
ball2 = sphere(pos=vector(5, 0, 0), radius=0.5, color=color.blue)
ball3 = sphere(pos=vector(0, 5, 0), radius=0.5, color=color.green)
ball4 = sphere(pos=vector(0, -5, 0), radius=0.5, color=color.yellow)
ball5 = sphere(pos=vector(0, 0, 5), radius=0.5, color=color.purple)
ball6 = sphere(pos=vector(0, 0, -5), radius=0.5, color=color.white)
v1 = vector(1,0,0)
v2 = vector(-1,0,0)
v3 = vector(0,-1,0)
v4 = vector(0,1,0)
v5 = vector(0,0,-1)
v6 = vector(0,0,1)

while True:
    rate(100)
    ball1.pos += v1 * 0.1
    ball2.pos += v2 * 0.1
    ball3.pos += v3 * 0.1
    ball4.pos += v4 * 0.1
    ball5.pos += v5 * 0.1
    ball6.pos += v6 * 0.1
    if mag(ball1.pos - ball2.pos) < (ball1.radius + ball2.radius):
        v1, v2 = v2, v1
    if mag(ball3.pos - ball4.pos) < (ball3.radius + ball4.radius):
        v3, v4 = v4, v3
    if mag(ball5.pos - ball6.pos) < (ball5.radius + ball6.radius):
        v5, v6 = v6, v5