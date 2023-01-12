import time
"""
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

inicio = time.perf_counter_ns()
# Para imprimir los 10 primeros números de la serie de Fibonacci
print(fibonacci(20))
fin = time.perf_counter_ns()
tiempo_total = (fin - inicio) / 1000000
print(f"Tiempo de ejecución: {tiempo_total:.2f} milisegundos")
"""

def fibonacciRecursividad(par01, num, num2):
    if par01 == 0:
        return 0
    else:
        if par01 == 1:
            return 1
        else:
            if par01 == 2:
                return num
            else:
                anterior = num
                num = num + num2
                num2 = anterior
                par01 = par01 - 1
                return fibonacciRecursividad(par01, num, num2)

inicio = time.perf_counter_ns()
num = fibonacciRecursividad(800, 1, 0)
fin = time.perf_counter_ns()
print(num)
tiempo_total = (fin - inicio) / 1000000
print(f"Tiempo de ejecución: {tiempo_total:.2f} milisegundos")

