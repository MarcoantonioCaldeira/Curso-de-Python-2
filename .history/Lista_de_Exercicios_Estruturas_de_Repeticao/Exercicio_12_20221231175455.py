quant_num = 0
soma = 0

while True:

    num = int(input("Digite um numero: "))
    quant_num += 1

    soma = soma + num
    if quant_num > 1:
        resposta = str(input("Deseja continuar?S/N: "))

        if resposta == 'N':
            break

print("Soma total: " + soma)
