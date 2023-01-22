import random
jogador = int(input('Digite um valor'))
computador = random.randint(0, 10)
soma = 0
par = soma % 2 == 0
while True:
    pi = str(input('P/I: ')).strip().upper()
    if pi in 'Pp':
        jogador = par