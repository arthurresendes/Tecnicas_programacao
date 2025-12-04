from random import randint,choice,sample


for i in range(5):
    print(randint(1,101))

lista = [1,2,3,4,5,6,7,8,9,10]
print(choice(lista))
print(sample(lista,5))

import random
random.seed(42)
first_random_number = random.randint(1, 100)
print(f"First random number with seed 42: {first_random_number}")
random.seed(100)
second_random_number = random.randint(1, 100)
print(f"Second random number with seed 100: {second_random_number}")