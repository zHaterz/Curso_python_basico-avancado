print(f'---Calculadora de Numeros inteiros!---')

cont = 0

try:
    numero_pri = input("Digite um numero:")
    numero_sec = input("Digite outro numero:")
    
    
    operadores = input("Digite um operador\n ( * | + |- | / ): ")
    
    conver_01 = int(numero_pri)
    conver_02 = int(numero_sec)
    
    while cont < 1:
        if operadores == "*":
            soma_valores = conver_01 * conver_02
            print(f'A multiplicação dos numeros é {soma_valores}')
            cont+=1
            
        elif operadores == "+":
            soma_valores = conver_01 + conver_02
            print(f'A soma dos valores é {soma_valores}')
            cont+=1
            
        elif operadores == "-":
            soma_valores = conver_01 - conver_02
            print(f'A subtração dos valores é {soma_valores}')
            cont+=1
            
        elif operadores == "/":
            soma_valores = conver_01 / conver_02
            print(f'A divisão dos valores é {soma_valores}')
            cont+=1
        else:
            print('Tente novamente')
            cont+=1
except:
    print('Por favor! *Digite novamente com operadores validos!*')