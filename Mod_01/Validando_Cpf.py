"""
Calculo do primeiro dígito do CPF
CPF:096.086.637-09
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  096.086.637-09 (746824890)
   10  9  8  7  6  5  4  3  2
*  0   9  6  0  8  6  6  3  7
   0  81  48 0  48 30 24 9 14

Somar todos os resultados: 
0+81+48+0+48+30+24+9+14 = 254
Multiplicar o resultado anterior por 10
254 * 10 = 2540
Obter o resto da divisão da conta anterior por 11
2540 % 11 = 10
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 0
"""

CPF = '74682489070'
# CPF = '88711711019'

# Variavies
nove_digitos_1 = CPF[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
primeiro_digito_verificado = 0


# codigo primeiro digito cpf.
for digito in nove_digitos_1:
    resultado_digito_1+= (int(digito) * contador_regressivo_1)
    contador_regressivo_1-=1 
    
resultado =(resultado_digito_1 * 10) % 11
if resultado >= 10:
    resultado = 0
    primeiro_digito_verificado = resultado
else:
    primeiro_digito_verificado = resultado
    
# ------------------------------XXXXXXXXXXX------------------
"""
Calculo do segundo dígito do CPF
CPF: 096.086.637-09
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
#                           Codigo segundo digito
dez_digitos = CPF[:9] + str(primeiro_digito_verificado)
resultado_digito_2 = 0
segundo_digito_verificado = 0
contador_regressivo_2 = 11

for digitos_2 in dez_digitos:
    resultado_digito_2 += (int(digitos_2) * contador_regressivo_2)
    contador_regressivo_2-=1
    
    r_digito_2 = (resultado_digito_2 * 10) % 11
    if r_digito_2 >= 10:
        resultado = 0
        segundo_digito_verificado = r_digito_2
    else:
        segundo_digito_verificado = r_digito_2
        
ultimos_dois_digitos = str(primeiro_digito_verificado) + str(segundo_digito_verificado)
    
if ultimos_dois_digitos == CPF[9:]:
   print(f'Os ultimos dois digitos do CPF são:{ultimos_dois_digitos}')

else:
    print('CPF invalido!')
    

# perdão tamanho é a mal escita do codigo sao 2:38 da manhã e eu não ia conseguir dormi sem fazer isso aqui.


    
