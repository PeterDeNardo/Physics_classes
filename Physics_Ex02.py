from vpython import *
import math

scene.width = 800
scene.height = 800
scene.autoscale = 0
# scene.range = (770, 770, 770)
# scene.center = vector(100, -180, 0)

#OBJECTS

ball = sphere(pos=vector(0, -399, 0),
              radius=50,
              color=color.red,
              make_trail=True)
centre = sphere(pos=vector(0, 0, 0),
              radius=20,
              color=color.cyan,
              make_trail=True)

#VARIABLES

r = 400
t = 1
omega = (6.28)/t
dt = 0.01
rotations = 1

time = label(pos=vector(0, -570,0), text = "Time: ", height = 15)
nmrRotations = label(pos=vector(650, 0,0), text = "Time: ", height = 15)
ballPosX = label(pos=vector(0, -640,0), text = "Ball Position: ", height = 15)
ballPosY = label(pos=vector(0, -710,0), text = "Ball Position: ", height = 15)


finished = False
while not finished:
    rate(60)

    t += dt

    #POSITION EQUATION P=rCoswt + rSinwt
    cosValue = math.cos(omega*t)
    sinValue = math.sin(omega*t)

    xPosition = (r*cosValue)
    yPosition = (r*sinValue)

    #New Position Vector

    P = vector(xPosition, yPosition, 0)
    ball.pos = P

    if ball.pos.x >= 399.8:
        rotations += 1

    #Update variable outputs
    time.text = "Time: %1.f" % t + " seconds"
    nmrRotations.text = "Rotation: %1.f" % rotations
    ballPosX.text = "Ball.pos.x: %1.f" % ball.pos.x
    ballPosY.text = "Ball.pos.y: %1.f" % ball.pos.y