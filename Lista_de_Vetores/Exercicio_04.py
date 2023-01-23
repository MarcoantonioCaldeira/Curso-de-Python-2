
lista_consoantes = []
verificar_consoantes = 0

for cont in range(10):

    lista_consoantes.append(str(input("Digite uma letra: ")))
    verificar = lista_consoantes[cont]

    if verificar not in ('a', 'e', 'i', 'o', 'u'):
        verificar_consoantes += 1

print("A consoante eh: " + verificar)
print(verificar_consoantes)
