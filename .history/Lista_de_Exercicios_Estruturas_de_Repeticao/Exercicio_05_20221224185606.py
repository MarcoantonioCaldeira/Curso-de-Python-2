quant = int(input("Digite a quantidade de elementos: "))

cont = 0
maior = 0
menor = 0


while cont < quant:
    num = int(input("Digite um numero: "))
    print(num)
    cont += 1

    if cont == 1:
        maior == num
        menor == num

    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

print("Maior numero: {} , Menor numero: {}".format(maior, menor))
