word = 'Ola Mundo'


print(word.capitalize())
print('[' + word.center(20) + ']')

# Verificva se termina com certa sequencia e retorna true or false

print(word.endswith('al'))
if word.endswith('do'):
    print("Termina com do")
else:
    print("Nao")

print(word.find('ndo'))
print(word.find('a'))

# Verifica se tem digito e numeros ao mesmo tempo
print(word.isalnum())
print('Arthur01'.isalnum())

# Verifica se tem apenas letras
print("Oi".isalpha())
print(word.isalpha())
print('Arthur01'.isalpha())

# Verifica se tem apenas digitos
print("011006".isdigit())
print(word.isdigit())
print('Arthur01'.isdigit())

# Verifica se é tudo minuscula
print("Oi".islower())
print(word.islower())
print('arthur01'.islower())

# Verifica se tudo é maiuscula
print("OI".isupper())
print(word.isupper())
print('arthur01'.isupper())

# Verifica espacos 
print(" ".isspace())
print(word.isspace())
print('arthur01'.isspace())

# Join
print(",".join([word] + ["Arthur"]))

# Minuscula
print("OI".lower())

# Maiuscula
print("oi".upper())

# Title
print("oI".title())

# lstrip - remove espaços iniciais
print("[" + " oi".lstrip() + "]")

# replace
print("www.jose.com".replace("jose.com", "arthur.org"))

# rfind
print("tau tau tau".rfind("ta"))

# rstrip
print("[" + "oi ".rstrip() + "]")

#split
print(word.split())

# Startswith
print(word.startswith('do'))
if word.startswith('Ola'):
    print("Comeca com Ola")
else:
    print("Nao")

# strip -> tira espações em brancos iniciais e finais
print("[" + "   oi   ".strip() + "]")

# Inverte maiuscula para minusculka e vice  e versa
print(word.swapcase())

