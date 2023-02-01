boletim = []
continuar = True
while continuar:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp.lower() != 's' and resp.lower() != 'n':
        print('Resposta invalida, tente novamente!...')
        resp = str(input('Deseja continuar [S/N]: ')).strip().lower()
    if resp.lower().strip() == 'n':
        continuar = False
print('-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"MEDIA":<8}')
print('-' * 30)
for i, b in enumerate(boletim):
    print(f'{i:<4}{b[0]:<10}{b[2]:<8}')
while True:
    opc = int(input('Quais notas do aluno deseja ver (999 para encerrar): '))
    if opc == 999:
        print('Finalizado...')
        break
    if opc <= len(boletim) -1:
        print(f'Notas do(a) {boletim[opc][0]} são {boletim[opc][1]}')
