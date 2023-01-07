def potencia(a,b):
    if b <= 0:
        respuesta = 1
    elif b % 2 == 0:
        pot = potencia(a,b/2)
        respuesta = pot * pot
    else:
        pot = potencia(a,(b-1)/2)
        respuesta = pot * pot * a
    print(respuesta)
    return respuesta
potencia(3,3)