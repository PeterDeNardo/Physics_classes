from visual import *

a2 = 0.0

earth = sphere(radius =0.9, pos = (0, 0, 3.4),
               color = color.green, material = materials.emissive, make_trail = True)

moon = sphere(radius = 0.3, pos = (0, 0, 3.4),
            color = color.yellow, material = materials.emissive, make_trail = True)

l2 = local_light(pos = moon.pos, color = moon.color)

while True:
    rate(100)

    l2.pos = moon.pos = (3.4) * vector(earth.pos.x * 0.295, sin(a2)- earth.pos.y/2 * 1.15, cos(a2) + earth.pos.z/4 * 1.15 )
    a2 += 0.055

    earth.pos.x += 0000000000.1
