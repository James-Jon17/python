num = []
impares = []
pares = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'Sua lista completa é {num}')
print(f'Sua lista de pares é {pares}')
print(f'Sua lista de impares é {impares}')