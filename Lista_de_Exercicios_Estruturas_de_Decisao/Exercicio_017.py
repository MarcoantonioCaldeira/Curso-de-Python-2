num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > num2:
    print("O maior numero é: {} , e o menor é: {}".format(num1, num3))
elif num2 > num1:
    print("O  maior numero é: {}, e o menor é: {}".format(num2, num3))
elif num3 > num2:
    print("O maior numero é: {}, e o menor é: {}".format(num3, num1))
