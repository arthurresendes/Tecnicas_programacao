print(2==2)
print(2 == 2.)
print(1==2)

while True:
    try:
        n = int(input("Digite um numero inteiro: "))
        break
    except:
        print("Digite um numero inteiro!!")

if n > 100:
    print(True)
else:
    print(False)