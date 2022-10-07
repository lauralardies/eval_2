from coche import Coche
from camioneta import Camioneta
from bicicleta import Bicicleta
from motocicleta import Motocicleta

c = Coche("azul", 4, 150, 1200)
ca = Camioneta("blanca", 4, 120, 1200, 6000)
b = Bicicleta("amarilla", 2, "deportiva")
m = Motocicleta("verde", 2, "urbana", 170, 1200)

vehiculos = [c, ca, b, m]
print(vehiculos)