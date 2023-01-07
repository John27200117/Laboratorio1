def pasos(n):
    if n == 1 or n == 2:
        return n
    return pasos(n-1)+pasos(n-2)
robot = pasos(5)
print(robot)
