class Alumnos():

    def __init__(self):

        dato1 = input("Introduzca el nombre del alumno: ")
        dato2 = input("Introduzca la nota del alumno: ")
        if dato1.isalpha():
            if dato2.isdigit():
                dato2 = int(dato2)
                if 0<=dato2<=10:
                    self.nombre = dato1
                    self.nota = dato2
                    print("El alumno se ha creado con éxito.")
        
        else:
            print("Debe introducir datos válidos.")
    
    def __str__(self):
        return print(self.nombre, self.nota)
            
    def calificacion(self):
        if self.nota >= 5:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha suspendido")

alumno1 = Alumnos()
alumno2 = Alumnos()
alumno3 = Alumnos()

alumno1.__str__()
alumno2.__str__()
alumno3.__str__()