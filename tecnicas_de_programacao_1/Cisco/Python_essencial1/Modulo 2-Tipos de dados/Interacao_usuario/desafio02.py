

while True:
    try:
        num = int(input("Digite um numero inteiro: "))
        if isinstance(num,int):
            break
    except Exception as e:
        print(f"Digite um numero intero corretamente. Erro: {e}")


calculo = 1/num + 1 / num + 1/ num + 1/num
print(calculo)