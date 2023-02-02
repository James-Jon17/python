classeA = []
aluno = {}
continuar = True
while continuar:
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        aluno['situação'] = 'Aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Reprovado'
    classeA.append(aluno.copy())
    resp = str(input('Deseja continuar? [N] para: '))
    if resp in 'Nn':
        continuar = False
for a in classeA:
    for i, v in a.items():
        print(f'{i}: {v}', end=' ')
    print()
print('-' * 30)
for k, v in aluno.items():
    print(f'{k} = {v}')