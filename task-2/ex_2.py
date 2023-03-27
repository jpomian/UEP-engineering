import math

# kwadrat

from asyncio.proactor_events import _ProactorSocketTransport


a=10
size=a*4
surface=a**2

print('[Kwadrat] Obwód: ' + str(size) + ' Pole: ' + str(surface))

# prostokat

a=5
b=8
size=(a*2)+(b*2)
surface=a*b

print('[Prostokat] Obwód: ' + str(size) + ' Pole: ' + str(surface))

# kolo

r=10
PI=math.pi
size=2*r*PI
surface=PI*r**2

print('[Kolo] Obwód: ' + str(round(size, 3)) + ' Pole: ' + str(round(surface, 3)))

# trapez rownoramienny

a=12
b=4
c=5
h=3

size=a+b+2*c
surface=(a*b)*h/2

print('[Trapez] Obwód: ' + str(size) + ' Pole: ' + str(surface))