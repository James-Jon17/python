lista = []
pos = 0 #quis começar a contagem do zero mas ignorei o(esqueci)
for cont in range(0, 5):
    pos += 1
    lista.append(int(input(f'Digite um valor para a posição {pos-1}: ')))
print('=-'*30)
print('Você digitou os valores: ', end='')
for lis in lista:
    print(lis, end=' ')
print(f'\nSeus numeros em uma lista fica {lista}')
print(f'\nO maior valor foi {max(lista)} na posição', end=' ')
for i, v in enumerate(lista): # mostrar as posições em que se repete o valor
    if v == max(lista):
        print(f'{i}...', end=' ')
print(f'\nO menor numero foi {min(lista)} na posição', end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end=' ')