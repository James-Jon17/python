import random
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    resposta = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} e o total foi {resposta}.', end= ' ')
    print('Deu Par' if resposta % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if resposta % 2 == 0:
            print('Jogador venceu')
            v += 1
        else:
            print('Computador venceu')
            break
    elif tipo == 'I':
        if resposta % 2 == 1:
            print('Você venceu')
        else:
            print('Computador venceu')
            break
    else:
        print('[ERRO] Você fez uma escolha invalida, tente novamente.')
    print('Vamos jogar novamente')
print(f'Gamer over, você venceu {v} vezes')
