from time import sleep


def apresentacao():
    print('=-' * 20)
    print('Contando de 1 até 10 pulando de 1 em 1')
    sleep(1)
    for n in range(1, 11):
        print(n, end=' ')
        sleep(0.5)
    print('fim')
    print('=-' * 20)
    print('Contando de 10 até 0 pulando de 2 em 2')
    sleep(1)
    for n in range(10, -1, -2):
        print(n, end=' ')
        sleep(0.5)
    print('fim')
    print('=-' * 20)
    print('Agora é a sua vez de personalizar a contagem!')


def contagem(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print('=-' * 20)
    print(f'Contando de {ini} até {fim} pulando de {pas} em {pas}')
    sleep(1)
    if ini < fim:
        for n in range(ini, fim+1, pas):
            print(n, end=' ')
            sleep(0.5)
        print('fim')
        print('=-' * 20)
    else:
        for n in range(ini, -fim+1, -pas):
            print(n, end=' ')
            sleep(0.5)
        print('fim')
        print('=-' * 20)

#apresentacao()
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)
