variable1=19
variable2="belen" 
variable3=True #belen
variable4=None
comparacion=variable=19
print(comparacion)
print(variable)#None

variable=1 
comparacion=variable==1 
print(comparacion)
comparacion=not comparacion
print(comparacion)
mayor=variable>0
print(mayor)
menor=variable<=0
print(menor)

mayor=(1+1)>1
menor=(20-30)<10
y=mayor and menor 
print(y)

print("ingrese un numero")
numero1=int(input())
numero2=int(imput("ingrese otro numero"))
suma=(numero1+numero2)
print("la suma de estos numeros da",suma)
menor=numero1 < numero2
mayo= numero1 > numero2 
igual= numero1 == numero2 
if mayor:
    print("numero1 es mayor que numero2")
if igual:
    print("numero1 es igual que numero2")   
if menor:
    print("numero1 es menor que numero2")   

#lista
lista=[0,1,2,3,4,5,6,7]   
for elemento in lista [:]:
    lista[elemento]=elemento*2
    print(lista[elemento],end=",")
print("")

for x in range (10):
    print(x)

for x in range(1,7,2):
    print(lista[x])
