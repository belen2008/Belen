
    print("hola")
numeroa=0
boleano=true 
while numero<150:
    print("ingrese un numero")
    numero=int(input(":"))
    numerodoble=numero*2
    print(numerodoble,end=",") 
    boleano=numero ==32
cree un programa que siga pidiendo numeros entre el 1 y el 100 hasta que adivines el numero.como pista
tiene que decir que el numero que ingresaste es mayor o menor al que tiene que adivinar 
 
import random 

numero_secreto = random.randint(1,100)
noAdivinado = true 

def rangoCorrecto(num):
    minimo=1
    maximo=100
    return minimo>num>maximo 

while noAdivinado:
    numeroIngresado = int(imput("Adivina el numero(entre 1 y 100):"))
    if rangoCorrecto(numeroIngresado):
       print("Por favor,ingresa un numero entre 1 y 100.")
       continue
    if numeroIngresado < numero_secreto:
        print("El numero es mayor.")
    if numeroIngresado > numero_secreto:
        print("El numero es menor.")
    if numeroIngresado == numero_secreto:
        print("¡Felicidades!Has adivinado el numero.")
        noAdivinado = false 