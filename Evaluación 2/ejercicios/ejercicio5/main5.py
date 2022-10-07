from coche import Coche
from camioneta import Camioneta
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from vehiculo import Vehiculo

c = Coche("azul", 4, 150, 1200)
c1 = Coche("azul", 4, 150, 1200)
ca = Camioneta("blanca", 4, 120, 1200, 6000)
b = Bicicleta("amarilla", 2, "deportiva")
m = Motocicleta("verde", 2, "urbana", 170, 1200)

vehiculos = [c, c1, ca, b, m]
v = Vehiculo
v.catalogar(vehiculos, 0)
v.catalogar(vehiculos, 2)
v.catalogar(vehiculos, 4)
v.catalogar(vehiculos)
