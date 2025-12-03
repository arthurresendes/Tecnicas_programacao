def mysplit(palavra: str) -> list[str]:
    palavra_final = []
    palavra_atual = ""
    for c in palavra:
        if c != ' ':
            palavra_atual += c
        else:
            if palavra_atual:
                palavra_final.append(palavra_atual)
                palavra_atual = "" # Zera palavra
    if palavra_atual:
        palavra_final.append(palavra_atual)
    return palavra_final

print(mysplit("O mundo tem que ser mais feliz"))