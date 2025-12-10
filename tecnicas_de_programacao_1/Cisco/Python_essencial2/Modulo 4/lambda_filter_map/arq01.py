num = lambda x: x * 2
print(num(2))

lista = [1,2,3,4,5,6,7,8,9,10]
mapiando = list(map(lambda x: x * 2, lista))
print(mapiando)


filtrando = list(filter(lambda x: x %2 == 0  , lista))
print(filtrando)

lista_exemplo = [i for i in range(1,11)]
juncao_1 = list(map(lambda x: x * x, lista_exemplo))
print(juncao_1)
juncao_2 = list(filter(lambda x: x %2 == 0, juncao_1))
print(juncao_2)