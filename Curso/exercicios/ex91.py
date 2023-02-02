from random import randint
from operator import itemgetter
from time import sleep
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = []
print('Sorteando os Dados')
print('-'*30)
sleep(2)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1.5)
print('-'*30)
print('     Resultado do sorteio     ')
print('-'*30)
sleep(2)
for i, v in enumerate(ranking):
    print(f'{i+1}º {v[0]} com {v[1]} pontos no dado')
    sleep(1)