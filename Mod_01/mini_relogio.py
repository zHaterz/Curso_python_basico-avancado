hora_str = input('Digite o horario:')

try: 
    
    hora_int = int(hora_str)
    if hora_int > 0 and hora_int < 12:
        print(f'Bom dia, agora são {hora_int}Hrs') 

    elif hora_int >= 12 and hora_int < 18:
        print(f'Boa Tarde, agora são {hora_int}Hrs') 
        
    else:
        print(f'Boa noite, agora são {hora_int}Hrs')
        
except:
    print('Digite numeros inteiros.')