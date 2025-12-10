def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())


'''
a função inner() retorna o valor da variável que pode ser acessada dentro de seu escopo, uma vez que inner() pode usar qualquer uma das entidades à disposição de outer()
a função outer() retorna a própria função inner(), mais precisamente, retorna uma cópia da função inner(), aquela que estava congelada no momento da chamada de outer(); a função congelada contém seu ambiente completo, incluindo o estado de todas as variáveis locais, que também significa que o valor de loc será retido com sucesso, embora outer() tenha deixado de existir há muito tempo.
'''