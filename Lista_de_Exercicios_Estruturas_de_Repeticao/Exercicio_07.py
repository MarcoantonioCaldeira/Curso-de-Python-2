cont = 0
quant_num_par = 0
quant_num_impar = 0

while cont < 9:

    num = int(input("Digite um numero: "))

    if num % 2 == 0:
        quant_num_par += 1
    elif num % 2 >= 1:
        quant_num_impar += 1

    cont += 1

print("Numeros pares: {}".format(quant_num_par))
print("Numeros impares: {}".format(quant_num_impar))
