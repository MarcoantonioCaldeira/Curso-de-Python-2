# para se criar listas utilizamos [[]


string = 'ABCDE'


# indices  0     1         2           3    4
lista = [123, True, 'Marco Antonio', 1.2, []]

# Listas são a mesma coisa que vetores

# print(lista)
# print(lista[2])

# Manipulando listas de maneira avançada

lista = [1, 2, 3, 4, 5, 6, 7, 8]

lista.append("Marco")  # Adicionei meu nome na lista
nome = lista.pop()
del lista[-1]

lista.insert(100, 5)
print(lista[4])

lista_a = ['Marco', 'Luiz', 2, 3, 6]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
