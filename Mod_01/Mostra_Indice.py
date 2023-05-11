nome = ['Maria', 'Joana','Bruno', 'Gustavo','Pedro','Jorge','Raquel', 1,2]
nomes_recebidos = ''

cont = 0

for name in nome:
    nomes_recebidos = name
    if nomes_recebidos == name:
        print(f'O item "{nomes_recebidos}" tem o indice {cont}')
        cont+=1
    
    