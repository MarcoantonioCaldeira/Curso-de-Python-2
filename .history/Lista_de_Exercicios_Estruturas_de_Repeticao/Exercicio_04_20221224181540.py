

cont = 0
maior = 0

while cont < 5:
    num = int(input("Digite um numero: "))
    print(num)
    cont = cont + 1

if num == 1:
    maior = num 
    print("Maior numero: {}".format(maior))
elif num > maior:
    maior = num
    print("Maior numero: {}".format(maior))