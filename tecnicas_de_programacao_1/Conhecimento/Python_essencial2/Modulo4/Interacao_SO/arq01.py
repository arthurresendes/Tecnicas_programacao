import os
print(os.name)

'''
os.mkdir("diretorio_exemplo")
print(os.listdir())

os.mkdir("diretorio_exemplo/direitorio2_exemplo")
print(os.listdir())
'''
os.chdir("diretorio_exemplo")
print(os.getcwd())
os.chdir("direitorio2_exemplo")
print(os.getcwd())

# os.rmdir("direitorio2_exemplo")
# os.removedirs("diretorio_exemplo/direitorio2_exemplo")
print(os.listdir())

returned_value = os.system("mkdir diretorio_exemplo")
print(returned_value)