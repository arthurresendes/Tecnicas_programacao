import random
print(2+2)
'''
+ - Adição
- = Subtração
* = Multiplicação
/ -> Divisão
// -> Divisão inteiro
% -> Modulo
** -> Exponenciação
'''
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