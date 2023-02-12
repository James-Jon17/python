from time import sleep

print('=-' * 20)
print('Contagem de 1 atá 10 de 1 em 1')
for n in range(1, 11):
    print(n, end=' ')
    sleep(0.5)
print('fim')
print('=-' * 20)
print('Contagem de 10 até 1 de 2 em 2')
for n in range(10, -1, -2):
    print(n, end=' ')
    sleep(0.5)
print('fim')
print('=-' * 20)
