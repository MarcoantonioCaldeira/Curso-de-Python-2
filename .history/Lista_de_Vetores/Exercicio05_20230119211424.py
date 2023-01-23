par = []
impar = []
cont_num_par = 0
cont_num_impar = 0

for cont in 10:

    num = int(input("Digite um numero: "))
    num.append(num)

    if num % 2 == 0:
        cont_num_par += 1
