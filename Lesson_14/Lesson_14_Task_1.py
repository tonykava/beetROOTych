def logger(func):
    def wrapper(a, b):
        return f'{func}, {a}, {b}'
    return wrapper


@logger
def add(x, y):
    return x + y

print(add(4, 5))

