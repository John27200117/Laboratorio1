def sumaRecursiva(a,b):
    if b == 0:
        return a
    else:
        return sumaRecursiva(a,b-1)+1
n = sumaRecursiva(5,3)
print(n)