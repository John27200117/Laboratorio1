import random
def desordenar(lista, largo_lista,contador):
    if contador<largo_lista:
        numeroRandom = random.randint(contador,largo_lista-1)
        lista[contador],lista[numeroRandom] = lista[numeroRandom],lista[contador]
        desordenar(lista,largo_lista,contador+1)
A=[1,2,3,4,5,6,7,8,9]
desordenar(A,len(A),0)
print(A)
#sí es aleatorio, pues para comprobarlo lo unico que se debe hacer es ejecutar el programa varias veces.
#y este nos dará respuestas diferentes.
