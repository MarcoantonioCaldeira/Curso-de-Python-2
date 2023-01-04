numero = int(input('Digite um número: '))

lista_numeros = list(range(2, numero + 1))

primos = []

divisores = 0

for n in lista_numeros:
    for count in primos:
        if (n % count == 0):
            divisores += 1

    if divisores == 0:
        primos.append(n)

    divisores = 0

print(primos)
