#CLASE 28/5

def nombreDeFuncion(parametros,argumentos):
    print(parametros,argumentos)

nombreDeFuncion("esto es una funcion,",
                "esto es un argumento")

def ingresarNumero(mensaje):
     entrada = input(mensaje)
     esEntero = int(entrada)
     return esEntero

def sumarNumeros(numero1,numero2):
    suma = numero1 + numero2 
    print("la suma de estos numeros da ",suma)
    return suma

