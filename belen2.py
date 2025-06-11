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

def menor(numero1, numero2):
    menor = numero1 < numero2 
    if menor :
         print(numero1,"es menor que" ,numero2)
    return menor 

def mayor(numero1,numero2):
    mayor = numero1 > numero2 
    if mayor:
         print(numero1,"es mayor que",numero2)
    return mayor 

def igual(numero1,numero2):
    igual = numero1 == numero2
    if igual:
         print(numero1, "es igual a " ,numero2)
    return igual 

def rango(start,stop,step):
    for i in range(start, stop,step):
        print(i, end=",")

4/6 
listas= ["elemento de la lista 1","elemento de la lista 2"]

listas[1]=listas[0]
listas [0]="elemento de la lista 0"
print(listas)

# clase 11/6 

objeto = {
    "nombre": "belen",
    "edad": 17,
    "ciudad":"buenos aires",
}
objeto["cumple"]=date(2008,5,19)
hoy = date(2025,6,11)
objeto["edad"]= hoy.year - objeto["cumple"].year 
print("hola",objeto["nombre"])

def cumplehoy(fechadehoy,fechadenacimiento):
    mismomes = fechadehoy.month ==fechadenacimiento.month
    mismodia = fechadehoy.day == fechadenacimiento.day
    return mismoMes and mismoDia 

objeto2 = dict(nombre = " dania ",
               edad = 21,
               ciudad = "buenos aires",
               cumple = date(2004,2,25))
listadediccionarios = [
    objeto,
    objeto2,
    {
        "nombre":"pablo",
        "edad":55,
        "ciudad":"buenos aires",
        "cumple":date(1969,11,24),
        "hijos":(objeto,objeto2)
    }
]
print("quien es el primer elemento?",
      listadediccionarios[0]["nombre"])
