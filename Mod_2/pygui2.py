lista = []
tupla = ()
nada = None
string = ''
inteiro = 0
flutuante = 0.1
setado = set()
dicion = {}







def falsy(valor):
    return 'falsy' if not valor else 'truthy'


print(f"{lista} = {falsy(lista)}")
print(f'{tupla} = {falsy(tupla)}')
print(f'{nada} = {falsy(nada)}')
print(f'{string} = {falsy(string)}')
print(f'{inteiro} = {falsy(tupla)}')
print(f'{flutuante} = {falsy(flutuante)}')
print(f'{setado} = {falsy(setado)}')
print(f'{dicion} = {falsy(dicion)}')