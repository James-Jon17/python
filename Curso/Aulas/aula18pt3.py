galera = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    print('Dados adicionado com sucesso')
print(galera)
for dados in galera:
    print(f'{dados[0]} tem {dados[1]} anos de idade!')