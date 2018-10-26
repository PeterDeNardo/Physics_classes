from visual import *
#Lissjous3D
a2 = 0.0

b2 = sphere(radius = 0.3, pos = (0, 0, 3.4),
            color = color.yellow, material = materials.emissive, make_trail = True)

l2 = local_light(pos = b2.pos, color = b2.color)

while True:
    rate(100)

    l2.pos = b2.pos = (3.4) * vector(sin(2*a2) * cos(4*a2), sin(4*a2), cos(7*a2))
    a2 += 0.055
    
