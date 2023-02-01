boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    resp = str(input('Deseja continuar [S/N]: '))
    boletim.append([nome, [nota1, nota2], media])
    if resp in 'Nn':
        break
print('-' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, f in enumerate(boletim):
    print(f'{i:<4}{f[0]:<10}{f[2]:>8}')
while True:
    print('-' * 36)
    opc = int(input('Mostrar nota de qual aluno? (999 interromper)'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')