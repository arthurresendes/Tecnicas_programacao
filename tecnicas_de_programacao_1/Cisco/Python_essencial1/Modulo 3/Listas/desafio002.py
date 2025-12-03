'''
Imagine uma lista - não muito longa, não muito complicada, apenas uma lista simples que contém alguns números inteiros. Alguns desses números podem ser repetidos, e essa é a pista. Não queremos repetições. Queremos que eles sejam removidos.

Sua tarefa é escrever um programa que remova todas as repetições de números da lista. O objetivo é ter uma lista na qual todos os números não aparecem mais de uma vez.

'''

my_list = [1,8, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nova_lista =[]

for i in my_list:
    if i not in nova_lista:
        nova_lista.append(i)

nova_lista.sort()
print(nova_lista)