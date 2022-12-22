# Tabuada

num = int(input("Digite um numero de 1 até 10: "))

cont = 0
while True:
    if num <= 10:

        while cont <= 10:

            print("{} * {} = {}".format(num, cont, (num * cont)))
            cont = cont + 1

    elif num > 10:
        print("Numero invalido!!!")
        continue
