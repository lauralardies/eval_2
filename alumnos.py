from mailbox import NoSuchMailboxError


class Alumnos():

    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito.")
    
    def calificacion(self):
        if self.nota >= 5:
            print("El alumno ha aprobado.")
        else:
            print("El alumno ha suspendido")