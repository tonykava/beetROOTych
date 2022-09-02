from random import randint
b = randint(2, 10000)

#arr = [randint(1, b) for i in range(11)]

arr = []
i = 0
while i != 10:
    arr.append(randint(1, b))
    i += 1

print(arr)
print(max(arr))
