primeiro = int(input('Primeira termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo +1, razao):
    print(c, end=' ')