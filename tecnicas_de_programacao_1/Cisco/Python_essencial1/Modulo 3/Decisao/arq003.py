valor = float(input("Digite seu salario: "))
if valor > 5000:
    valor *= 1.10
    print(f"Imposto calculado: {round(valor,2)}")
else:
    print("Sem impostos")