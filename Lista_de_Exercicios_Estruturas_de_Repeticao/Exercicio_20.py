cont_alunos = 0
cont_turma = 0


while True:

    quant_alunos = int(input("Digite a quantidade de alunos: "))
    cont_alunos += 1

    if quant_alunos > 40:

        print("A quantidade de alunos por turma não pode ter de 40 alunos")

        continue

    else:

        quant_turma = int(input("Digite a quantidade de turmas: "))
        cont_turma += 1

        alunos_p_turma = quant_alunos / quant_turma

        print("Quantidade de alunos por turma: ", alunos_p_turma)
        print("Quantidade de turmas: ", quant_turma)

        desissao = str(input("Deseja continuar?: S/N"))

        if desissao == 'N':

            print("Programa finalisado com sucesso!!!")
            break
        else:

            continue
