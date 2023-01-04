num = int(input("Digite um numero inteiro: "))
i = 1
cont = 0
quant_divisoes = 0

while True:

    while i < num:
        if num % i == 0:
            cont += 1
            quant_divisoes += 1
