from random import randint
#a = [randint(1, 10) for i in range(1, 11)]
#b = [randint(1, 10) for j in range(1, 11)]
#print(set([i for i in a if i in b]))
a = []
b = []

i = 0
while i != 10:
    a.append(randint(1, 10))
    i += 1

j = 0
while j != 10:
    b.append(randint(1, 10))
    j += 1

print(a)
print(b)
print(set(a).intersection(b))
