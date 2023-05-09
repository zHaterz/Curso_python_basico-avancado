nome_user = input('Digite seu nome: ')

if len(nome_user) <= 4:
    print('Seu nome é curto!')

elif len(nome_user) >= 5 and len(nome_user) < 6:
    print('Seu nome é normal!')

else:
    print('Seu nome é grande!')