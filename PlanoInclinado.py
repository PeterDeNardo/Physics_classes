from vpython import *
import math

angulo = 60

floor = box(length=100, height=0.1, width=10, axis=vector(math.cos(math.radians(angulo)), math.sin(math.radians(angulo)), 0), color=color.white)

ball = sphere(pos= vector(0, 0.5, 0), color=color.red)
ball.velocity = vector(0, 0, 0)
m = 0.2
g = 1.0
p = m * g

dt = 0.05

px = 0
py = 0

while 1:
    rate(10)

    px += p * math.cos(math.radians(angulo))
    py += p * math.sin(math.radians(angulo))

    ball.velocity.y = -py
    ball.velocity.x = -px

    print(ball.velocity)

    ball.pos += ball.velocity * dt