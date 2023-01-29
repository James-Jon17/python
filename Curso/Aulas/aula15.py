lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for i in range(-1, -(len(lanche)+1), -1):
    print(lanche[i])

print('-'*30)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*30)

print('Eu irei comer {} com {}, depois uma {} com {}'.format(*lanche))

print('-'*30)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-'*50)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')


