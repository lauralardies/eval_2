class Producto():

    def __init__(self):
        dato1 = input("Introduzca el código del producto: ")
        dato2 = input("Introduzca el nombre del producto: ")
        dato3 = input("Introduzca el precio del producto: ")
        dato4 = input("Introduzca el tipo de producto: ")
        if dato2.isalpha() and dato4.isalpha():
            if dato3.replace(",", "", 1).isdigit() and dato1.isdigit():
                self.codigo = int(dato1)
                self.nombre = dato2
                self.precio = float(dato3)
                self.tipo = dato4
                print("El producto se ha creado con éxito.")
        else:
            print("Introdzca datos válidos.")
    
    def __str__(self):
        return print(self.codigo, self.nombre, self.precio, self.tipo)ç
    
producto = Producto()
producto.__str__()