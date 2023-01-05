cont_nota = 0
soma_nota = 0


while True:
    nota = int(input("Digite a sua nota: "))

    cont_nota += 1

    soma_nota = soma_nota + nota
    media = soma_nota/cont_nota

    if cont_nota > 1:
        resposta = input("Deseja parar S/N: ")

        if resposta == 'S':
            break
        else:
            continue

print("A media das notas é: ", media)
