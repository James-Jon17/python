resp = 's'
soma = cont = media = 0
while resp in 'Ss':
    numero = int(input('Digite um valor: '))
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / cont
print('Você digitou {} numeros a soma é {} e a media foi {:.2f}'.format(cont, soma, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))