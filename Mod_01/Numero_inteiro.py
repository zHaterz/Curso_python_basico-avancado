numero_str = input("Digite um numero inteiro: ")



try:
    numero_inteiro = int(numero_str)
    if numero_inteiro % 2 == 0:
        
        print(f'O numero {numero_inteiro} é par!')
        
    elif numero_inteiro % 2 != 0:
        
        print(f'O numero {numero_inteiro} é impar!')
     
except:
    print('Não é um numero inteiro!')