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
lista.sort(reverse=True)
print(f'O tamanho da sua lista foi {len(lista)}')
print(f'Os valores digitados foram {lista}')
if 5 in lista:
    print('O 5 foi encontrado na lista')
else:
    print('O 5 não foi encontrado na lista')
