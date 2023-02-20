ALUNOS = 10
NOTAS = 4

medias = []
media_sete = 0

for cont in range(ALUNOS):
    media = 0
    for cont_2 in range(NOTAS):
        media += float(input(f"Digite a nota {cont+1} do aluno {cont_2+1}: "))

    media /= NOTAS
    medias.append(media)

    if media >= 7:
        media_sete += 1

print("A media dos alunos foi: ")
for i in range(ALUNOS):
    print(f"Aluno {i+1}: {medias[i]}")

print(
    f"Os alunos que obtiveram media maior ou igual a sete são: \n{media_sete}")
