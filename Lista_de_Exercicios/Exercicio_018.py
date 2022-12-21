salario = int(input('Digite o valor do seu salario: '))

if salario <= 280:
    valor_aumento = (salario * 20)/100
    novo_salario = valor_aumento + salario
    print("Seu salario era: {} \n Novo salario: {}".format(salario, novo_salario))

elif salario > 280 and salario <= 700:
    valor_aumento = (salario * 15)/100
    novo_salario = valor_aumento + salario
    print("Seu salario era: {} \n Novo salario: {}".format(salario, novo_salario))

elif salario > 700 and salario <= 1500:
    valor_aumento = (salario * 10)/100
    novo_salario = valor_aumento + salario
    print("Seu salario era: {} \n Novo salario: {}".format(salario, novo_salario))

elif salario > 1500:
    valor_aumento = (salario * 5)/100
    novo_salario = valor_aumento + salario
    print("Seu salario era: {} \n Novo salario: {}".format(salario, novo_salario))
