class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)
    
    def catalogar(lista, ruedas = 0):
        if ruedas is 0:
            for objeto in lista:
                print(objeto.__class__.__name__)
                print(objeto)
        else:
            contador = 0
            for objeto in lista:
                if objeto.ruedas == ruedas:
                    contador = contador + 1
                    print("Se han encontrado {} vehículos con {} ruedas". format(contador, ruedas))
                    print(objeto.__class__.__name__)
                    print(objeto)
