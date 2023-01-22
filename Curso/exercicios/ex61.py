primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
quantidade = 0
while cont <= 10:
    print('{} '.format(termo), end=' ')
    termo += razao
    cont += 1
    quantidade += 1
    print(' = ' if cont > 10 else ' > ', end=' ')
print('Foram {} termos'.format(quantidade))
print('Fim')