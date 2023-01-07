def seleccionOrden(lista,largo_lista,contador):
    if contador<largo_lista:
        pequeño  = lista[contador]
        posicion = contador
        for i in range(contador+1,largo_lista):
            if lista[i]<pequeño:
                pequeño=lista[i]
                posicion=i
        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        seleccionOrden(lista,largo_lista,contador+1)
A=[4,1,6,8,3,2,5,9,7]
seleccionOrden(A,len(A),0)
print(A)