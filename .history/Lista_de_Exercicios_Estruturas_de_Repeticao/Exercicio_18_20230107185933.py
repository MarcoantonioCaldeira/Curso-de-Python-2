
cont_idade = 0
soma_idade = 0
media_idade = 0

while True:

    idade = type(input("Digite a sua idade: "))
    cont_idade += 1

    soma_idade = cont_idade + soma_idade
    media_idade = soma_idade / cont_idade

    if cont_idade > 1:

        desicao = input("Deseja continuar: S/N")

        if desicao == 'N':

            break
