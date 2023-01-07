cont_idade = 0
soma_idade = 0


while True:

    idade = int(input("Digite a sua idade: "))
    cont_idade += 1

    if cont_idade > 1:

        desicao = input("Deseja continuar: S/N")

        if desicao == 'N':

            break
