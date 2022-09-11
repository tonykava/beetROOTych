def function(a, b):
    return (int(a) ** 2) / int(b)

try:
    a = int(input('Give me a: '))
    b = int(input('Give me b: '))
    if b == 0:
        raise Exception('b cant be zero')
    print(function(a, b))
except ValueError:
    print('Input numbers should be integer')
