import random
a, n = list(input('Give me ur str: ')), 5
for i in range(n):
	random.shuffle(a)
	print(''.join(a))


