from visual import *
import math

angulo = 45.0 

floor = box(length=100, height=0.1, width=10, axis=vector(math.cos(angulo), math.sin(angulo) ,0), color=color.blue)

ball = sphere(pos=(0,0.5,0), color=color.red)
ball.velocity = vector(0,0,0)
m = 2.0
g = 1.0
p = m*g

dt = 0.05
while 1:
    rate(100)

    ax = g * math.sin(angulo)
    ay = g * math.cos(angulo)
    
    px = p * math.sin(angulo)
    py = p * math.cos(angulo)
    
    ball.velocity.y = -py * ay 
    ball.velocity.x = -px * ax

    ball.pos +=  ball.velocity*dt
    
