from errores import Error

numero = 7/0
lista = [4, 7, 30, 23, 5]
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
resultado = "2" + 10

Error.error_funct(numero)
Error.error_funct(lista[10])
Error.error_funct(paises["alemania"])
Error.error_funct(resultado)