from collections import deque
lista = ["celular", "computador", "tablet"]
nova_lista = lista.append("iphone")
print(lista)
print(nova_lista)
lista = deque()
lista.appendleft("celular")
lista.appendleft("computador")
lista.appendleft("tablet")
lista.appendleft("android")
print(lista)
lista.popleft()
lista.pop()
print(lista)