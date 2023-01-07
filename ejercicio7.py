def pasos(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return n+1
    return pasos(n-1)+pasos(n-2)+pasos(n-3)
robot = pasos(5)
print(robot)