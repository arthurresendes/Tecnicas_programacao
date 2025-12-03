def numero(ano:str, dia:str, mes:str):
    ano = list(ano)
    mes = list(mes)
    dia = list(dia)
    
    lista_ano = list(map(int, ano))
    lista_mes = list(map(int, mes))
    lista_dia = list(map(int, dia))
    soma = 0
    for i in lista_ano:
        soma += i
    for i in lista_mes:
        soma += i
    for i in lista_dia:
        soma += i
    
    result = str(soma)
    if len(result) > 1:
        listagem = list(result)
        convertendo = list(map(int, listagem))
        numero_vida = 0
        for i in convertendo:
            numero_vida += i
        return f"O número vida eh {numero_vida}"
    else:
        return f"O numero vida eh {soma}"



print(numero("1999","12","29"))
print(numero("2017","01","01"))
print(numero("2000","01","01"))