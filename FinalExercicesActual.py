from vpython import *
a2 = 0.0
earth = sphere(radius = 0.9, pos = vector(0, 0, 3.4),
               texture=textures.earth,  make_trail = True)
moon = sphere(radius = 0.3, pos = vector(0, 0, 3.4),
              texture=textures.metal,  make_trail = True)
sun = sphere(radius = 9, pos = vector(100, 0, 3.4),
             texture=textures.flower)
l2 = local_light(pos = moon.pos, color = moon.color)

sunDeath = False
growing = True

while True:
    rate(100)

    earth.rotate(angle = 1/20)
    moon.rotate(angle=1 / 30)
    sun.rotate(angle=1 / 100)

    if (earth.pos.x <= 100):
        l2.pos = moon.pos = (3.4) * vector(earth.pos.x * 0.295, sin(a2)- earth.pos.y/2 * 1.15, cos(a2) + earth.pos.z/4 * 1.15 )
        a2 += 0.055
        earth.pos.x += 0000000000.1

    elif (growing):
        sun.radius += 0.01

    if  (sun.radius >= 40) or sunDeath and (not sun.radius <= 4) and not growing :
        sunDeath = True
        growing = False
        sun.radius -= 0.02

    if  (sunDeath) and sun.radius == sun.radius <= 4:
        sun.color = color.yellow
        sun.radius += 0.1
