#print([i for i in range(1, 101) if i % 7 == 0 and i % 5 != 0])

arr = []
i = 1
while i != 101:
    if i % 7 == 0 and i % 5 != 0:
        arr.append(i)
        i += 1
    else:
        i += 1
print(arr)

