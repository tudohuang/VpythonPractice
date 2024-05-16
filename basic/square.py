from vpython import *


cube = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.red)

while True:
    rate(50)  
    cube.pos.x -= 0.03
    cube.pos.y -= 0.04
    cube.pos.z -= 0.02

