lista = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    print('Dados adicionados com sucesso!')
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
print()
print(f'Foram cadastrado {len(lista)} pessoas!')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}')
for p in lista:
    if p[1] == menor:
        print(f'Os menores são {p[0]}')