def game():
    print("oi")


def menu():
    while True:
        try:
            continuar = int(input(f"0. Sair - 1. Jogar novamente: "))
            if continuar == 1:
                game()
            elif continuar == 0:
                print("Saindo")
                break
            else:
                print("Digite o número correto")
        except ValueError:
            print("Digite 0 ou 1 apenas!")

menu()
