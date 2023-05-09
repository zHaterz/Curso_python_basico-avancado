name = input(str('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
altura_metro = float(input('Digte sua altura [m²]:'))

ano_nascimento = 2023 - idade

print(f'Nome:{name}\nIdade:{idade}\nSua altura é:{altura_metro}\nAno de Nascimento:{ano_nascimento}')
if idade >= 18:
    print('Você é maior de idade :)')
else:
    print("Você é menor de idade ;)")

