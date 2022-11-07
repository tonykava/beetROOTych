def mult(a, n):
    if n < 0:
        raise ValueError('This function works only with positive integers')
    if n != 0:
        return a + mult(a, n - 1)
    else:
        return 0

if __name__ == '__main__':
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))

