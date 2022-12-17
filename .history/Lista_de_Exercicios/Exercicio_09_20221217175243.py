#Calculo IMC

nome = input("Digite o seu nome: ")

peso = int(input("Digite o seu peso: "))

altura = float(input("Digite a sua altura: "))

valor_imc = peso / (altura * altura)

print("O valor do IMC é: {}!".format(valor_imc))

if valor_imc >= 40:
    print("Obesidade morbida")


