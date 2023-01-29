#data da tabela 25/01/2023

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'Améria-MG', 'Botafogo', 'Santos', 'Góias', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('Os 5 primeiros colocados são:\n')
for colodado in range(0, 5):
    print(f'{colodado+1}. {brasileirao[colodado]}')

print('-'*20)

print('Os 4 ultimos são:\n')
for ultimo in range(-4, -0, +1):
    print(f'{ultimo+5}. {brasileirao[ultimo]}')

print('-'*20)
print('A lista em ordem alfabetica é: ')
brasileirao_sem_aspas = ', '.join(map(str, sorted(brasileirao)))


print(brasileirao_sem_aspas)
print('-'*20)
print(f'O Corinthians está na posição {brasileirao.index("Corinthians")+1}ª')

