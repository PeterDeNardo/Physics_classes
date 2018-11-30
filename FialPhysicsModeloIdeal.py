## This can be run from a python shell by typing
##    import orbit
## or from unix command line with
##    python orbit.py
from visual import *

## By default, "visual" creates a 3-D object called scene
scene.autoscale=0
scene.range=2

## create three objects, set their initial
##   position, radius, color, and other
##   properties: mass, momentum("p")
giant = sphere()
giant.pos = vector(-0.201,0.020,0)
giant.radius = 0.09 ; giant.color = color.green
giant.mass = 1
giant.p = vector(0, 0.051, -0.01) * giant.mass

moon = sphere()
moon.pos = vector(0,0.5,0.5)
moon.radius = 0.04 ; moon.color = color.white
moon.mass = 0.00125
moon.p = 0.035 * -giant.p

## tweak initial condition so that total momentum is zero
giant.p -= giant.p

## create 'curve' objects showing where we've been
for a in [giant, moon]:
  a.orbit = curve(color=a.color, radius = 0.01)


def pstep( giant, moon ): 
  dist = moon.pos - giant.pos
  force = G * giant.mass * moon.mass * dist / mag(dist)**3
  giant.p = giant.p + force*dt
  moon.p = moon.p - force*dt
  dist = moon.pos - giant.pos

dt = 0.01
G = 1 
while 1:
  ## set the picture update rate (100 times per second)
  rate(1000)
  #giant.pos.x += 1
  pstep( giant, moon )
  giant.pos.x += 0.001

  for a in [giant, moon]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)

## For an intro to visual python see
## http://wiki.aims.ac.za/mediawiki/index.php/Vpython:Getting_Started
