velocidade = int(input('Digite a velovidade do seu veiculo: '))

RADAR_1 = 60 #constante

if velocidade > RADAR_1:
    print("Seu carro está acima da velocidade!!!")
else:
    print("Seu carro está abaixo da velocidade!!!")