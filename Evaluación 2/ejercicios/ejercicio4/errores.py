error = 7/0
def error(error):
    try:
        error
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except IndexError:
        print("Puede ser que el índice indicado no exista en al lista.")
