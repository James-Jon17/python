listagem = ('Lapis', 1.75,
            'borracha', 2,
            'caderno', 19.90,
            'estojo', 25,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'caneta', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('-' * 40)