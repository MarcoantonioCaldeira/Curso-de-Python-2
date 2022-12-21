nota = int(input("Digite a sua nota entre 0 e 10: "))

cont = 0

while cont <= nota:

    if nota > 10:
        print("Nota invalida!!!")
        input("Digite a nota novamente: ")
        break

cont = cont + 1
