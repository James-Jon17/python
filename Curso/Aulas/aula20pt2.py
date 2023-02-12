def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
    print(f'A soma A + B = {s}')


#Programa P
soma(3, 5)
soma(4, 8)

print('-' * 30)


def contador(* num):
    print(f'O tamanho do parametro {len(num)}')
    print(f'Os parametros são:', end=' ')
    for c in num:
        print(c, end=' ')


contador(4, 6, 'Jota', 0)
