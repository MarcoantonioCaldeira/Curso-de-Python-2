quant_num = 0

while True:

    num = int(input("Digite um numero: "))
    quant_num += 1

    if quant_num > 1:
        resposta = str(input("Deseja continuar?: S/N"))

    if resposta == 'N':
break
