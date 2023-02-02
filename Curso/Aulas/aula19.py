pessoas = {'Nome': 'Jota', 'Sexo': 'Masculino', 'Idade': 23}
del pessoas['Sexo'] #apagado do dicionario
pessoas['Nome'] = 'João'
pessoas['Peso'] = 80.1
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
print('-' * 30)
for k in pessoas.values():
    print(k)
print('-' * 30)
for k, v in pessoas.items():
    print(f'{k}: {v}')
