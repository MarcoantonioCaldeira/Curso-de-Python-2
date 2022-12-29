quant_num = int(
    input("Digite a quantidade de numeros que voce deseja somar: "))


count = 0


while count < quant_num:
    num = int(input("Digite um numero: "))
    soma = num + num

    print("O valor da soma é: {}".format(num))
    count += 1
