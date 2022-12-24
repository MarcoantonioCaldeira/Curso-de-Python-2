quant = int(input("Digite a quantidade de elementos: "))


cont = 0

while cont < quant:
    num = int(input("Digite um numero: "))
    print(num)
    cont += 1

    maior = 0
    menor = 0

    if num == 1:
        maior == num
        menor == num

    elif num > maior:
        maior == num

    elif num < menor:
        menor == num
