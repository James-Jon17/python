def maior(* num):
    if len(num) == 0:
        num = (0,)
    print('=-' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
    print(f'Foram {len(num)} valores analisados.')
    print(f'E o maior valor é {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
