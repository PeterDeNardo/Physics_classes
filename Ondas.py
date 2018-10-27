from visual import *

a2 = 0
a3 = 0
bola = sphere(radius=0.000000000003, make_trail=True, pos=(0, 0, 3.4), color=color.yellow)

while True:
    rate(100)
    bola.pos = (-10)*vector(bola.x, sin(a2*2), a3)
    a2 += 0.05
    a3 += 0.01
