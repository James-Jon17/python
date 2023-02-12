jogador = {}
partida = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
if tot != 0:
    for c in range(0, tot):
        partida.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'A campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i+1} o jogador fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')