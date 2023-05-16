# Exercício - sistema de perguntas e respostas
import os
import emoji

cont_ac = 0
cont_er = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


quest_1 = perguntas[0]
quest_2 = perguntas[1] 
quest_3 = perguntas[2]


# Primeira parte concluida, escrita do codigo ficou uma bagunça, irei criar outro com ajuda do instrutor.


# Questão 1 - concluida.
while True:
    
    print('Desafio de Perguntas')
    
    try:
        primeira_questao = quest_1.get('Pergunta')
        op_um = quest_1.get('Opções')
        
        print(f'Pergunta: {primeira_questao}')
        entrada_um = input(f'Opções:\n{op_um}: ')
        os.system('clear')
        if int(entrada_um) == 4:
            resp_um = quest_1.get('Resposta')
            print(f'Resposta: {resp_um}\nAcertou!')
            cont_ac += 1
        else:
            print('Errou')
            cont_er += 1
            
        # Segunda Pergunta do codigo! 
        
        segunda_questao = quest_2.get('Pergunta')
        op_dois = quest_2.get('Opções')
        
        print(f'Pegunta: {segunda_questao}')
        entrada_dois = input(f'Opções\n{op_dois}: ')
        
        os.system('clear')
        if int(entrada_dois) == 25:
            resp_dois = quest_2.get('Resposta')
            print(f'Resposta:{resp_dois}\nVocê Acertou!')
            cont_ac += 1
        else:
            print('Você Errou!')
            cont_er +=1
            
        # Terceira Questão
        
        terceira_questao = quest_3.get('Pergunta')
        op_tres = quest_3.get('Opções')
        print(f'Pergunta:{terceira_questao}')
        entrada_tres = input(f'Opções:{op_tres}: ')
        
        os.system('clear')
        
        if int(entrada_tres) == 5:
            resp_tres = quest_3.get('Resposta')
            print(f'Resposta:{resp_tres}\nVocê Acertou!')
            cont_ac+=1
        else:
            print(f'Você errou!')
            cont_er +=1
            
        os.system('clear')
        
        print(f'Acertou:{cont_ac}\nErrou:{cont_er}')
        break
    except:
        print('Por favor apenas numeros!')
    
    
    
    