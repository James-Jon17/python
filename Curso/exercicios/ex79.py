lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor já inserido! Não farei novamente...')
    r = str(input('Deseja continuar [S/N]: ')).lower().strip()[0]
    if r in 'Nn':
        break
print('=-' * 30)
lista.sort()
print(f'Os valores digitados foram {lista}')