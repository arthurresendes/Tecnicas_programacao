def calcular_media(dicionario: dict):
    soma = 0
    for i ,j in dicionario.items():
        soma = sum(j)
        media = soma / len(j)
        if media > 6.0:
            print(f"O {i} Passou (Média: {media:.2f})")
        else:
            print(f"O {i} Não Passou (Média: {media:.2f})")

aluno = {"Arthur": [6,7,8], "Jose": [1,2,3], "Gabriel": [5,9,8]}
calcular_media(aluno)