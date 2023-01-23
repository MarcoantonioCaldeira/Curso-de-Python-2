# Exercicio de calculo de media

lista_notas = []
media = 0

print("Media das notas")

for cont in range(4):
    lista_notas.append(float(input("Digite a sua nota " + str(cont+1) + ": ")))
    media += lista_notas[cont]

media = media/4

# print(lista_notas)
print(media)
