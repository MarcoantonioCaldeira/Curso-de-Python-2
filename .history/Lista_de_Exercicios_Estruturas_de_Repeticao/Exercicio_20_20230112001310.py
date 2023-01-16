cont_alunos = 0
cont_turma = 0

while True:

    quant_alunos = int(input("Digite a quantidade de alunos"))
    cont_alunos += 1

    if quant_alunos > 40:

        print("A quantidade de alunos por turma não pode ter de 40 alunos")

        break
    else:

        quant_turma = int(input("Digite a quantidade de turmas"))
