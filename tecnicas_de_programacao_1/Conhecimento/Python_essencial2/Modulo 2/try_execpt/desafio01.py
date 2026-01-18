def le_valor():
    while True:
        try:
            var = int(input("Digite um valor entra -10 e 10: "))
            if var < 11 and var > -11:
                break
        except:
            print("Erro, digite corretamente!!")
    print(f"O numero é {var}")


le_valor()