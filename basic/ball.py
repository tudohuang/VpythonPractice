from vpython import *

ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.red) #pos = 原點, radius =半徑, color =紅色

for i in range(10000):
    rate(50)
    ball.pos.x += 0.1
