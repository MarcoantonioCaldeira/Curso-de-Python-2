nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

print("A media do aluno eh: {}".format(media))

if media >= 6:
    print("Aluno aprovado!!!")
elif media <= 5 and media >= 4:
    print("Aluno em exame final")
else:
    print("Aluno reprovado")
