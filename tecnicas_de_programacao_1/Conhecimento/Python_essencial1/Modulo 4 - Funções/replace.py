numero = 1500
result = f"R$ {numero:.2f}"
result = result.replace(".",",")
print(result)
print(type(result))