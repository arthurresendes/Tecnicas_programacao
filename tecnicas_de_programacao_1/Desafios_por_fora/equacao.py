def delta(a:int,b:int,c:int):
    delta = b ** 2 - 4 * a * c
    return delta
   
import math  
def valor_x(a:int,b:int, c:int):
    result = delta(a,b,c)
    x1 = (-b + math.sqrt(result)) / (2 * a)
    x2 = (-b - math.sqrt(result)) / (2 * a)
    return x1, x2


def calcula():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
   
    resultado_delta = delta(a,b,c)
    resultado_x1 , resultado_x2 = valor_x(a,b,c)
   
    equacao1 = a * resultado_x1 ** 2 + b * resultado_x1 + c
    equacao2 = a * resultado_x2 ** 2 + b * resultado_x2 + c
   
    return f"Resultado da equacao 1: {equacao1}\nResultado da equacao 2: {equacao2}"

print(calcula())