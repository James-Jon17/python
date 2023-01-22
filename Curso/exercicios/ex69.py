tot18 = pessoas = homens = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas += 1
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break
print(f'apenas {pessoas} pessoa foi registrada' if pessoas < 2 else f'Foram {pessoas} pessoas registrada')
print(f'Total de pessoa(s) com mais de 18 anos: {tot18}')
print(f'teve {homens} homem registrado' if homens < 2 else f'Foram {homens} homens registrado')
print(f'E foram {totM20} mulheres com menos de 20 anos')
