# O usuario entra com o numero!!!
num = int(input("Digite um numero e veja se ele é primo: "))

if num > 1:  # verifica se num é maior que 1

    for i in range(2, num):  # cria uma lista do numero 2 pra cima
        if num % i == 0:  # Verifica se o numero é divisivel por outros numeros
            print(num, 'não é primo')

            def divisores(num):  # Vamos ver se o numero é ou não primo!!!
                for i in range(1, num//2+1):
                    if num % i == 0:
                        yield i
                yield num

            num = 47587950

            print("Seus divisores são: ", list(divisores(num)))
            break
    else:
        print(num, 'é primo')  # Se não ele é primo

elif num == 0:
    print(num, 'é zero')

elif num == 1:
    print(num, 'é um')

else:
    print(num, 'é negativo')
