'''
etapa 1: criar uma lista vazia chamada beatles;
etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
etapa 3: solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.
'''

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
while True:
    nome1 = input("Adicione o Stu Sutcliffe: ")
    if nome1 == "Stu Sutcliffe":
        beatles.append(nome1)
        break
while True:
    nome2 = input("Adicione o Pete Best: ")
    if nome2 == "Pete Best":
        beatles.append(nome2)
        break

del beatles[3]
del beatles[3]

beatles.insert(0,"Ringo Starr")
print(beatles)