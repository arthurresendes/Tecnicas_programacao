from random import randint,choice,sample


for i in range(5):
    print(randint(1,101))

lista = [1,2,3,4,5,6,7,8,9,10]
print(choice(lista))
print(sample(lista,5))