class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)
    
    def catalogar(lista):
        
        for objeto in lista:
            print(objeto.__class__.__name__)
            print(objeto)