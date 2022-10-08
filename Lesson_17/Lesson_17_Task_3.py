def answer(up, down):
    if up == down:
        return 1
    if up > down:
        n = up // down
        up = up % down
        while up % 3 == 0 and down % 3 == 0:
            up //= 3
            down //= 3
        while up % 2 == 0 and down % 2 == 0:
            up //= 2
            down //= 2
        while up % 5 == 0 and down % 5 == 0:
            up //= 5
            down //= 5
        while up % 7 == 0 and down % 7 == 0:
            up //= 7
            down //= 7
        if up == 0:
            return n
        return '{} and {}/{}'.format(n, up, down)
    else:
        while up % 3 == 0 and down % 3 == 0:
            up //= 3
            down //= 3
        while up % 2 == 0 and down % 2 == 0:
            up //= 2
            down //= 2
        while up % 5 == 0 and down % 5 == 0:
            up //= 5
            down //= 5
        while up % 7 == 0 and down % 7 == 0:
            up //= 7
            down //= 7
        return '{}/{}'.format(up, down)


class Fraction:

    def __init__(self, up, down):
        self.up = up
        self.down = down
        if self.down == 0:
            raise ZeroDivisionError
        if self.down < 0:
            raise Exception('Only numerator can be negative')
        if self.up == 0:
            raise Exception('Numerator cannot be ZERO!')

    def __add__(self, other):
        if self.down == other.down:
            return answer(self.up + other.up, self.down)
        else:
            su = self.up * other.down
            ou = other.up * self.down
            sd = self.down * other.down
            s = su + ou
            return answer(s, sd)

    def __sub__(self, other):
        if self.down == other.down:
            return answer(self.up - other.up, self.down)
        su = self.up * other.down
        ou = other.up * self.down
        sd = self.down * other.down
        s = su - ou
        return answer(s, sd)

    def __truediv__(self, other):
        su = self.up * other.down
        sd = self.down * other.up
        return answer(su, sd)

    def __mul__(self, other):
        su = self.up * other.up
        sd = self.down * other.down
        return answer(su, sd)

    def __eq__(self, other):
        return (self.up / self.down) == (other.up / other.down)

    def __ne__(self, other):
        return (self.up / self.down) != (other.up / other.down)

    def __lt__(self, other):
        return (self.up / self.down) < (other.up / other.down)

    def __le__(self, other):
        return (self.up / self.down) <= (other.up / other.down)

    def __gt__(self, other):
        return (self.up / self.down) > (other.up / other.down)

    def __ge__(self, other):
        return (self.up / self.down) >= (other.up / other.down)


f1 = Fraction(1, 3)
f2 = Fraction(5, 3)
print(f1 + f2)
print(f1 - f2)
print(f1 / f2)
print(f1 * f2)
print(f1 == f2)
print(f1 != f2)
print(f1 < f2)
print(f1 <= f2)
print(f1 > f2)
print(f1 >= f2)
