# Declarando as variaveis
quant_num = 0
soma = 0
maior = 0
menor = 0
cont_num = 0

while True:

    num = int(input("Digite um numero: "))  # O usuario entra com um numero!!!
    quant_num += 1  # Aqui é feito a contagem de limite de numeros

    soma = soma + num  # Aqui é feita a soma dos numeros

    cont_num += 1  # Aqui é feito a contagem de todos os numeros

    # Verificacao de valores
    if cont_num == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

    if quant_num > 1:
        resposta = str(input("Deseja continuar?S/N: "))

        if resposta == 'N':
            break  # Finalizando o programa

# Exibindo valores
print("Soma total: ", soma)
print("O maior numero é: ", maior)
print("O menor numero é: ", menor)
