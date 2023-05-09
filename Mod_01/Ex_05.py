nome = 'Anderson'

qt_str = len(nome)
ast = 'x'


cond = 0

novo_nome = ''


while cond < qt_str:
    str_name = nome[cond]
    novo_nome += f'*{str_name}'
    cond+=1
    
print(f'{novo_nome}')
 
    