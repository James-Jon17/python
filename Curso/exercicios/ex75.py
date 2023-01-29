while True:
    num = (int(input('Digite um numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite mais um numero: ')))
    if len(num) <= 5:
       break
print(f'Os numeros escolhidos foram: {num}')
print(f'O numero apareceu 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1}ª')
else:
    print(f'O valor 3 não foi digitádo em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
