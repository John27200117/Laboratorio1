import time
def factorialRecursivo(n):
    if n==1:
        return 1
    return n*factorialRecursivo(n-1)
tiempo1 = time.perf_counter()
A = factorialRecursivo(5)
tiempo2 = time.perf_counter()
print(A,"-se hizo en: ",tiempo2-tiempo1)

def factorial(n):
    b=1
    for i in range(n,1,-1):
        b=b*i
    return b
tiempo1 = time.perf_counter()
B = factorial(5)
tiempo2 = time.perf_counter()
print(B,"- se hizo en: ",tiempo2-tiempo1)

