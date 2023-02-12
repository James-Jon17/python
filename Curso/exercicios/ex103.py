def ficha(jog='<desconhacido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeaonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)