meu_numero = []
multi = 1
divisao = 1
sub = 1

print("Informe 5 numeros")


for cont in range(5):

    num = (float(input("Digite um numero: ")))
    meu_numero.append(num)

soma = sum(meu_numero)
multi = multi * num
divisao = num / divisao
sub = num - sub

print("A soma é: ", soma)
print("A multiplicacao é: ", multi)
print("A divisao é: ", divisao)
print("A subtracao é: ", sub)
