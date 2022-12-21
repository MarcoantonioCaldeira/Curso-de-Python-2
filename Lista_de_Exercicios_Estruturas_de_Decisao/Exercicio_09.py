# Calculo IMC

nome = input("Digite o seu nome: ")

peso = int(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura: "))

valor_imc = peso / (altura * altura)

print("O valor do IMC é: {}!".format(valor_imc))

if valor_imc >= 18 and valor_imc <= 25:
    print('Peso ideal')
elif valor_imc >= 25 and valor_imc <= 30:
    print('Acima do peso')
else:
    print('Obesidade Morbida')


# elif = else if
