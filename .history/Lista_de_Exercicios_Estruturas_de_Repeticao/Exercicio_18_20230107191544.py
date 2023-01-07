
cont_idade = 0
soma_idade = 0

while True:

    idade = int(input("Digite a sua idade: "))
    cont_idade += 1

    soma_idade = idade + soma_idade
    media_idade = soma_idade/cont_idade

    if cont_idade > 1:
        desicao = input("Deseja continuar: S/N")

        if desicao == 'N':
            break

print("A media de idade da populacao eh: ", media_idade)
