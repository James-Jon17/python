def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'nessa volta os valores são {valores} num recebe {num} e a soma dos anteriores temos {s}')


soma(2)
soma(2, 3)
soma(2, 3, 5)
soma(2, 3, 5, 10)
