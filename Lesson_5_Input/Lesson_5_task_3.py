from itertools import permutations
import random
a = input('Give me your str: ')
n = 5
for i in range(n):
    print(random.choice([''.join(i) for i in permutations(list(a))]))


