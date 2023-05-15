import math

class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a+self.b+self.c

    def pole(self):
        return 0

# trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_szefa = Trojkat(4, 3, 5, 4)
print(trojkat_szefa.obwod())

class Kolo:
    def __init__(self, r):
        self.r = r

    def obwod(self):
        return (2*self.r*math.pi)

    def pole(self):
        return (math.pi*self.r**2)

kolo_mistrza = Kolo(12)
print(kolo_mistrza.obwod())
print(kolo_mistrza.pole())