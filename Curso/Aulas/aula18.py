teste = []
teste.append('Jota')
teste.append(25)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
teste[0] = 'Paulo'
teste[1] = 23
galera.append(teste)
print(galera)