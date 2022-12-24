

cont = 0
maior = 'maior'

while cont < 5:
    num = int(input("Digite um numero: "))
    print(num)
    maior = num

    cont = cont + 1
    if num > maior:
        maior = num

print("Maior numero: {}".format(maior))
