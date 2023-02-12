dadosP = {}
registro = []
continuar = True
while continuar:
    registro.append(str(input('Nome: ')))
    while True:
        sexo = str(input('Sexo [M/F]: ')).lower().strip()
        if sexo == 'f' or sexo == 'm':
            break
        print('ERRO! Sexo invalido, apenas M ou F.')
    registro.append(sexo)
    registro.append(int(input('Idade: ')))
    registro.append(dadosP.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]: ')).lower().strip()
        if continuar == 'n' or continuar == 's':
            break
        print('Erro! Resposta invalida, apenas S ou N.')
    if continuar == 'n':
        break
    dadosP.copy()
print(registro)
print(dadosP)
