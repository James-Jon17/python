#ChatGPT me mostrou


import random


def maior(* num):
    if len(num) == 0:
        num = (0,)
    print('=-' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
    print(f'Foram {len(num)} valores analisados.')
    print(f'E o maior valor é {max(num)}')


quantidade_argumentos = random.randint(1, 10)
argumentos = [random.randint(1, 10) for i in range(quantidade_argumentos)]
maior(*argumentos)