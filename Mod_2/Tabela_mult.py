
print('Tabuada dos numeros:')
while True:
    entrada = input('Digite um numero ou [S] para sair: ')
    
    if entrada[0].lower() == 's':
        break
    
    try:
        if entrada:
            for i in range(1,11):
                resultado = int(entrada) * i 
                print(f'{entrada} x {i} | {resultado}')
    except:
        print('Algo deu errado meu mano!\ncomeça de novo ai.')