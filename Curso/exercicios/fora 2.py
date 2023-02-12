for c in range(1, 101):
    saida = "Fizz" if c % 3 == 0 else ""
    saida += "Buzz" if c % 5 == 0 else ""
    print(saida if saida else c)