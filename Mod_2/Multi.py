
# Multiplica os valores, passados no parametro.
def multi(*num):
    tot = 1 
    for i in num:
        tot*=i
    return tot
        
# Identifica se um numero é IMPAR ou PAR.
def check(a):
    if a % 2 == 0:
        print(f'O numero {a} é um PAR!')
    else:
        print(f'O numero {a} é um IMPAR! ')
        
          
numeros = 5,2
mult_1 = multi(*numeros)

check(mult_1)



