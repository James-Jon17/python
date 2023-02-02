aluno = str(input('Nome do aluno: '))
media = float(input(f'Media do {aluno}: '))
print(f'- O nome é igual {aluno}')
print(f'- A média é igual a {media}')
if media <= 3:
    print('- Situação é igual a reprovado')
elif media >= 5 < 7:
    print('- Situação é igual a recuperação')
elif media >= 7 <= 10:
    print('- Situação é igual a aprovado')