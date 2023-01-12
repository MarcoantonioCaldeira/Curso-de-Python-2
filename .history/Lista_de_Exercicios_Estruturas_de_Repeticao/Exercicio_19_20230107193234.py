num_candidatos = int(input("Digite o numero total de eleitores: "))
cont = 0
cont_num_votos = 0

while cont < num_candidatos:

    valor_candidato = int(
        input("Em qual candidato voce deseja votar?: 1, 2 ou 3: "))
    cont_num_votos += 1
