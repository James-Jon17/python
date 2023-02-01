num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
sorted(num[0])
sorted(num[1])
print('=-' * 30)
print(f'Os numeros páres digitados foram: ', end='')
for pares in num[0]:
    print(f'{pares}', end=' ')
print(f'\nOs numeros impares digitados foram: ', end='')
for impares in num[1]:
    print(f'{impares}', end=' ')