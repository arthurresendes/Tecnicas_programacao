word = 'Ola mundo'
print(len(word))

multiline = '''Line #1
Line #2'''

print(len(multiline))

char1 = 'a'
char2 = 'z'
print(ord(char1))
print(ord(char2))


print(chr(97))
print(chr(105))

print(word[1:3])

print('a' in word)
print('j' in word)
print('a' not in word)
print('j' not in word)

print(min("aAbByYzZ"))
print(max("aAbByYzZ"))

print(word.index('a'))
print(list(word))

word = word.lower()
print(word)
print(word.count('o'))