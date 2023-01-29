valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('\n')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print(f'\nSua lista é', end=' ')
for o in valores:
    print(o, end=' ')