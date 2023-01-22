loja = 'Loja do Super Jotao'
print('-'*30)
print(loja.center(30))
print(('-'*30))
total = totmil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    total += valor
    cont += 1
    if valor >= 1000:
        totmil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    conitnuar = ' '
    while conitnuar not in 'SN':
        conitnuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if conitnuar == 'N':
        break
print('acabou')
print(f'O total da compra foi R${total:.2f}')
print(f'Foram {totmil} que custa mais de mil reais')
print(f'O menor produto custa R${menor:.2f} e foi {barato}')