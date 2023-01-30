lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Numero já adicionado a lista')
        if n % 2 == 0:
            lista_par.append(n)
        else:
            lista_impar.append(n)

    r = str(input('Deseja continuar [S/N]: '))
    if r in 'Nn':
        break
print('=-'*30)
print(f'Sua lista tem {len(lista)} elementos e os numeros que fazem parte são {lista.sort()}')
print(f'Sua lista apenas com os numeros pares {lista_par.sort()}')
print(f'Sua lista apenas com numeros impares {lista_impar.sort()}')