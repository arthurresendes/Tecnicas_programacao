while True:
    try:
        hora = int(input("Digite a hora atual: "))
        if hora >= 0 and hora <= 23:
            break
    except:
        print("Digite em formato de numero inteiro")
        hora = int(input("Digite a hora atual: "))
 
while True:  
    try:
        minuto = int(input("Digite o minuto atual: "))
        if minuto >= 0 and minuto <= 60:
            break
    except:
        print("Digite em formato de numero inteiro")
        minuto = int(input("Digite o minuto atual: "))

try:
    duracao = int(input("Digite a duracao: "))
except:
    print("Digite em formato de numero inteiro")
    duracao = int(input("Digite a duracao: "))


minuto += duracao
quiocente, resto = divmod(minuto,60)
hora += quiocente
minuto = resto
hora = hora % 24

print(f"Ira acabara as {hora:02d}:{minuto:02d}")