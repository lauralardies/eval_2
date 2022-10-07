from curses.ascii import isalpha


class Producto():

    def __init__(self):
        dato1 = input("Introduzca el código del producto: ")
        dato2 = input("Introduzca el nombre del producto: ")
        dato3 = input("Introduzca el precio del producto: ")
        dato4 = input("Introduzca el tipo de producto: ")
        if dato1.isalpha() and dato2.isalpha() and dato4.isalpha():
            if dato3.replace(",", "", 1).isalpha():
                self.codigo = dato1
                self.nombre = dato2
                self.precio = float(dato3)
                self.tipo = dato4
                print("El producto se ha creado con éxito.")
    
    def __str__(self):
        return print(self.codigo, self.nombre, self.precio, self.tipo)