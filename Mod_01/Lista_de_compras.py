import os


lista_de_compras_usuario = []
# ind = enumerate(list(lista_de_compras_usuario))

while True:
    print('Selecione uma Opção')
    entrada = input('[a] Adicionar | [r] remover | [l] listar: ')
    os.system('clear')
    
    if entrada[0].lower() == 'a':
        valor_usuario = input('Valor:')
        os.system('clear')
        lista_de_compras_usuario.append(valor_usuario)
    
    elif entrada[0].lower() == 'l':
        for cont, item in enumerate(lista_de_compras_usuario):
            print(cont, item)
        if len(lista_de_compras_usuario) == 0:
            print('Não contem nada na lista')
    
    elif entrada[0].lower == 'r':
        remover = input('Qual item deseja remover')
        lista_de_compras_usuario.remove(remover)
    