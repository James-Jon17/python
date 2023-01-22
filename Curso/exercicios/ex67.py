while True:
    n = int(input('Digite a tabua de que deseja ver: '))
    if n < 0:
        print('-'*30)
        print('Você encerrou o programa!')
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-'*30)
