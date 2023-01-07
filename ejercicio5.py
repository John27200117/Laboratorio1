import time
def fibonacciRecursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return fibonacciRecursivo(numero-1)+fibonacciRecursivo(numero-2)
tiempo1 = time.perf_counter()
fibonacciRecursivo(8)
tiempo2 = time.perf_counter()
print("Fibonacci recursivo demoró: ",tiempo2-tiempo1)

def fibonacci(n):
    a = 0
    b = 1
    for k in range(n+1):
        c = b+a
        a = b
        b = c
    return a
tiempo1 = time.perf_counter()
fibonacci(8)
tiempo2 = time.perf_counter()
print("Fibonacci No recursivo demoró: ",tiempo2-tiempo1)
