from random import randint
n = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'os valores sorteados foram: ', end='')
for numero in n:
    print(f'{numero}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)} \nO menor valor foi {min(n)}')
