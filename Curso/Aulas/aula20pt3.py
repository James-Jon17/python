def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 5, 6, 4]
dobra(valores[:])
dobrado = valores
dobra(dobrado)
print(valores)
print(dobrado)
