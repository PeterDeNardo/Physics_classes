
from vpython import *
import random

initialHeight = 4.5
initialVelocity = random.randint(-50, 0)
Angle = random.randint(10, 30)
LaAngles = random.randint(-50, 50)

sk = 1

def newLaunch(ball) :
    ball.pos = vector(0,2,60)
    iH = 4.5
    iV = random.randint(10, 100)
    A = random.randint(10, 180)
    LA = random.randint(-90, 90)
    v = [iH, iV, A, LA]

    return v



rod1 = cylinder(pos = vector(-20,0,0),
               axis = vector(0,15,0),
               radius = 1)

rod2 = cylinder(pos = vector(+20,0,0),
               axis = vector(0,15,0),
               radius = 1)

rod3 = cylinder(pos = vector(-20,15,0),
               axis = vector(40,0,0),
               radius = 1)

myplace = box(size = vector(100,1,150))

ball = sphere(pos = vector(0,2,60),
              radius = 1,
              color = color.red,
              make_trail = True)

v = newLaunch(ball)

initialHeight = v[0]
initialVelocity = v[1]
Angle = v[2]
LaAngles = v[3]


while True:

    t=0
    dt = 0.1
    g = -45

    Fgrav = vector(0, g*dt,0)


    ballV = vector(LaAngles,
                   initialVelocity*sin(Angle*pi/180),
                   -180)
                   #initialVelocity * cos(Angle * pi / 180))

    while True:
        rate(30)
        ballV = ballV + Fgrav
        ball.pos += ballV*dt
        if ball.pos.y < 0:
            v = newLaunch(ball)
            initialHeight = v[0]
            initialVelocity = v[1]
            Angle = v[2]
            LaAngles = v[3]
            break

        if abs(ball.pos.y - rod1.pos.y)<=sk:
            v = newLaunch(ball)
            initialHeight = v[0]
            initialVelocity = v[1]
            Angle = v[2]
            LaAngles = v[3]
            break

