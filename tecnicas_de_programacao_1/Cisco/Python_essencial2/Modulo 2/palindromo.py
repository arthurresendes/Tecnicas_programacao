

def palindormo(palavra: str) -> bool:
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    print(palavra_invertida)
    if palavra_invertida == palavra:
        return True
    else:
        return False

print(palindormo("Roma é amor"))