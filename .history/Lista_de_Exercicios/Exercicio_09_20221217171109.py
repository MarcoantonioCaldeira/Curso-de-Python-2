#Calculo IMC

nome = input("Digite o seu nome: ")

peso = input("Digite o seu peso: ")

altura = input("Digite a sua altura: ")

valor_imc = peso / (altura * altura)

print("O valor do IMC é: {}!".format(valor_imc))