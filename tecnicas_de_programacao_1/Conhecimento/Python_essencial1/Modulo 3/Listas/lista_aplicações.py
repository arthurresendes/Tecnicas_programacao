lista = [i * i for i in range(5)]
print(lista)

condicao = [i * 2 for i in range(10) if i %2 ==0]
print(condicao)

from random import randint
duas_listas = [[i + randint(1,101) - i for i in range(1,6)] for j in range(5)]
print(duas_listas)

