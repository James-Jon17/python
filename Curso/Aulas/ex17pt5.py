a = [2, 3, 4, 7]
b = a[:] #copia e não liga
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')