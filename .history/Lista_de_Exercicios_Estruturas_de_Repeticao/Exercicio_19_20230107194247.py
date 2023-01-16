num_candidatos = int(input("Digite o numero total de eleitores: "))
cont = 0
cont_num_votos = 0
cont_voto_1 = 0
cont_voto_2 = 0
cont_voto_3 = 0

while cont < num_candidatos:

    valor_candidato = int(
        input("Em qual candidato voce deseja votar?: 1, 2 ou 3: "))
    cont_num_votos += 1

    if valor_candidato == 1:
        cont_voto_1 += 1

    elif valor_candidato == 2:
        cont_voto_2 += 1

    elif valor_candidato == 3:
        cont_voto_3 += 1

    cont += 1

print("Total de votos ao condidato 1: ", cont_voto_1)
print("Total de votos ao condidato 2: ", cont_voto_2)
print("Total de votos ao condidato 3: ", cont_voto_3)

if cont_voto_1 > cont_voto_2 and cont_voto_3:
    print("O candidato 1 venceu!!!")

elif cont_voto_2 > cont_voto_1 and cont_voto_2:
