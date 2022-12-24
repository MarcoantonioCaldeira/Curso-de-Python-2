

cont = 0

while cont < 5:
    num = int(input("Digite um numero: "))
    print(num)
    cont = cont + 1

maior = 0
menor = 0

if  maior > menor:
    print('Maior numero {}'.format(maior))
elif menor > maior:
    print('Maior numero {}'.format(menor))
elif num > menor:
    print('Maior numero {}'.format(num))
elif num > maior:
    print('Maior numero: {}'.format(num))

