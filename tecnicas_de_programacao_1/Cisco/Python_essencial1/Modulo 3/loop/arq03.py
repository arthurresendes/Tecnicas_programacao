palavra = input("Digite uma palavra: ").upper()


for i in palavra:
    if i in "AEIOU":
        continue
    else:
        print(i, end="")