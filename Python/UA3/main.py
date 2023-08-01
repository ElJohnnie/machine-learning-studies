import math

class Circulo:
   def __init__(self, x, y, raio):
       self.x = x
       self.y = y
       self.raio = raio

   def area(self):
       return math.pi * self.raio ** 2

   def diametro(self):
       return self.raio * 2

   def circunferencia(self):
       return 2 * math.pi * self.raio

   def mover(self, x, y):
       self.x = x
       self.y = y

   def __str__(self):
       return f'Círculo: centro = ({self.x}, {self.y}), raio = {self.raio}'