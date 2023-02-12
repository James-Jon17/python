for c in range(1, 101):
    if c % 3 == 0 and c % 5 == 0:
        print(f'{c} FizzBuzz')
    elif c % 3 == 0:
        print(f'{c} Fizz')
    elif c % 5 == 0:
        print(f'{c} Buzz')
    else:
        print(c)