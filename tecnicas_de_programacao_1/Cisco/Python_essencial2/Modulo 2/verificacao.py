def verifica(palavra1: str, palavra2: str):
    for letra in list(palavra1):
        if letra not in palavra2:
            return "False"
    return "Yes"


print(verifica("donor", "Nabucodonosor"))