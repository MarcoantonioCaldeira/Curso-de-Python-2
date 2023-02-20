meu_numero = []
cont_numero = 0

print("Informe 5 numeros")


for cont in range(5):

    num = (int(input("Digite um numero: ")))
    meu_numero.append(num)

soma = sum(meu_numero)

print("A soma é: ", soma)
