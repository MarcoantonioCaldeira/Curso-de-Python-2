NUMEROS = 20
par = []
impar = []
num_inteiro = []


for cont in range(NUMEROS):

    num = int(input("Digite um numero: "))
    num_inteiro.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
print ("Numeros Inteiros")
for num in num_inteiro:
    print(num)
