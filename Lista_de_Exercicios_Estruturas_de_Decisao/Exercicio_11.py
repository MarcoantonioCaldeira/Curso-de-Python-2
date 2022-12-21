
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}') #função para mostrar nome invertido

    if ' ' in nome:#Ira verificar se o nome contem ou não espaços
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')#len é uma função que é usada para contar o numero de caracteres 
    print(f'A primeira letra do seu nome é {nome[0]}')#funcão para mostrar a primeira letra do nome
    print(f'A última letra do seu nome é {nome[-1]}')#funcão para mostrar a ultima letra do nome
else:
    print("Desculpe, você deixou campos vazios.")