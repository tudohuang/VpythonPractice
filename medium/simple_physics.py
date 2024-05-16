from vpython import sphere, vector, color, rate, gcurve, sin, cos, pi


ball = sphere(pos=vector(1, 0, 0), radius=0.1, color=color.red)
graph = gcurve(color=color.blue)

"""
Args:
L -> Length
θ -> Radian(degrees * pi/180°)
ω -> degree velocity
dt -> timestamp
g -> 9.8
"""
length = 1.0
theta = pi / 4  
omega = 0.0     
g = 9.8         
dt = 0.01       

"""
Formula:
    alpha = -g/L * sin(theta) #角加速度
    omega = omega + alpha * dt
    theta = theta + omega * dt
    x = L * sin(theta)
    y = -L * cos(theta)
"""
while True:
    rate(100)
    alpha = -g / length * sin(theta)  
    omega += alpha * dt             
    theta += omega * dt              
    ball.pos = vector(length * sin(theta), -length * cos(theta), 0)  
    graph.plot(pos=(length * sin(theta), -length * cos(theta)))  
