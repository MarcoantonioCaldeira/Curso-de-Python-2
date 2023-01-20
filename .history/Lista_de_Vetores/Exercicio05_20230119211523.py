NUMEROS = 20
par = []
impar = []
num_inteiro = []
cont_num_par = 0
cont_num_impar = 0

for cont in range(NUMEROS):

    num = int(input("Digite um numero: "))
    num_inteiro.append(num)

    if num % 2 == 0:
        cont_num_par += 1
