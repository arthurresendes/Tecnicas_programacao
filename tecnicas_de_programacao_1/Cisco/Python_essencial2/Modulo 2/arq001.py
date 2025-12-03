var = 0

assert var == 0

try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

x = '\''
print(len(x))

print(ord('c') - ord('a'))


print(chr(120))

print('Mike' > "Mikey")



try:
    print(float("1, 3"))
except ValueError:
    print("Erro ValueError")