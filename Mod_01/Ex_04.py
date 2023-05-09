
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if nome and idade:
    print(f'Seu nome é {nome}, você tem {idade} anos.')
    print(f'Seu nome invertido é {nome[::-1]}') 
    print(f'Seu nome contem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    ult = len(nome)
    print(f'A ultima letra do seu nome é {nome[-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços.')
    else:
        print('Seu nome não contem espaços.')
    
else:
    print(f'Você não preencheu todos os dados!')