# Criar uma função que duplica,triplica,quadrupilca um valor.

# def dois(num):
#     dupli = int(num) * 2
#     return dupli

# def tripli(num):
#     triplica = int(num) * 3
#     return triplica

# def quadru(num):
#     quadruplica = int(num) *  4
#     return quadruplica


def multiplicador(multiplcidor):
    def multiplicar(numero):
        return multiplcidor * numero
    return multiplicar

duplica = multiplicador(2)
tripli = multiplicador(3)
quadruplica = multiplicador(4)
    
numeros = input('Digite um numero para\n(2x | 3x | 4x): ') 
dois = duplica(int(numeros))
tres = tripli(int(numeros))
quatro = quadruplica(int(numeros)) 


print(dois, tres, quatro)
        
        