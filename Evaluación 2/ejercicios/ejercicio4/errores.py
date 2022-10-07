

error ="2" + 10

def error_funct(error):
    try:
        error
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except IndexError:
        print("Puede ser que el índice indicado no exista en al lista.")
    except KeyError:
        print("La llave marcada no existe en el diccionario.")
    except TypeError:
        print("Estás sumando un str")
