# não foi feito por mim
import random
from time import sleep
for x in range(int(input('Number of games: '))):
    #sleep(1.5)
    print(f'Game {x+1}: {random.sample(range(1, 60), 6)}')