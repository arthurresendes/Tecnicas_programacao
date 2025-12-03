def anagrama(palavra1:str,palavra2:str) -> None:
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()
    cont = 0
    if len(palavra1) == len(palavra2):
        for i in palavra2:
            if i in palavra1:
                cont += 1
        if cont == len(palavra2):
            print("Eh anagrama")
        else:
            print("Não eh anagrama")
    else:
        print("Nao eh anagrama")

anagrama("listen", "silent")
anagrama("modern", "norman")