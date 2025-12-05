def lista_num(n:int) -> list:
    lista_letras = []
    if 1 <= n <= 26:
        for i in range(1,n + 1):
            valor = chr(ord('A') + i - 1)
            lista_letras.append(valor)
        return lista_letras
    else:
        return "Número fora do intervalo (1-26)"
   

num = int(input("Digite um numero entre 1 até 26 para ver suas respectivas letras: "))
print(lista_num(num))