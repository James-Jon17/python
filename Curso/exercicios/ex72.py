estenco = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezessei', 'dezessete', 'dezoito', 'dezenove', 'vinte']
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= valor <= 20:
        break
    print('Valor invalido! tente novamente.', end=' ')
print(f'você digitou o número {estenco[valor]}')
