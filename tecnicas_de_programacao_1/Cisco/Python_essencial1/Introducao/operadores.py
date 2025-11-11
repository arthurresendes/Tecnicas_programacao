import random
'''
+ - Adição
- = Subtração
* = Multiplicação
/ -> Divisão
// -> Divisão inteiro
% -> Modulo
** -> Exponenciação
'''
print(2+2)
print(1/1)
print(1//2 * 3)
print(4%11)
z = y = x = 1
print(x, y, z, sep='*')
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)


num1 = random.randint(1,101)
num2 = random.randint(1,1001)
print(num1,num2)


dict = {
    "Adição": num1 + num2,         
    "Subtração": num1 - num2,         
    "Multiplicação": num1 * num2,         
    "Divisão": num1 / num2,         
    "Divisão inteira":num1 // num2,        
    "Modulo":num1 % num2,       
    "Exponenciacao":num1 ** num2
}
print(dict)
