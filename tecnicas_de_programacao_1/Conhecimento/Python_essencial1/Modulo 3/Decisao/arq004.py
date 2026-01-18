def calcular_ano(ano):
    if ano % 4 != 0:
        print("é um ano comum")
    elif ano % 100 != 0:
        print("ano bissexto")
    elif ano % 400 != 0:
        print("é ano comum")
    else:
        print("ano bissexto")


ano = int(input("Digite o ano: "))
calcular_ano(ano)