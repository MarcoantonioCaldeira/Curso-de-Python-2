

cont = 0
maior = 0

while cont < 5:
    num = int(input("Digite um numero: "))
    print(num)

    if num == 1:
        maior = num
    elif num > maior:
        maior = num
        print("Maior numero: {}".format(maior))

    cont = cont + 1
