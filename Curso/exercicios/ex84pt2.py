dados = []
temp = []
continuar = True
#mai = men = 0
while continuar:
    temp.append(str(input('Nome: ').title()))
    temp.append((int(input('Idade: '))))
    dados.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar [S/N]: ')).lower().strip()
    #while resp not in 'SsNn':
    while resp.lower() != 'sim' and resp.lower() != 'não': #(tentei pegar a primeira instancia da letra mas desse modo n da)
        print('Resposta invalida. Por favor, informe "sim" ou "não".')
        resp = str(input('Deseja continuar [S/N]: ')).lower().strip()
    if resp.lower().strip() == 'não': #or 'n' or 'N':
        continuar = False

print('Dados coletados')
for d in dados:
    print(f'Nome: {d[0]}, Idade: {d[1]}')
idade = [dado[1] for dado in dados]
idade_ordenada = sorted(idade, reverse=True)
print('Idades ordenadas em crescimento')
print(f'Os mais velhos são com {idade_ordenada[:2]}')



