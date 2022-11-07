def to_power(x, exp):
    if exp < 0 :
        raise ValueError('This function works only with exp > 0')
    if exp != 0:
        return x * to_power(x, exp - 1)
    else:
        return 1

if __name__ == '__main__':
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    print(to_power(2, -1))

