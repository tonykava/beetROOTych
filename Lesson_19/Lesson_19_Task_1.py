class with_index:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.index:
            raise StopIteration
        else:
            self.start += 1
            return (self.start - 1, self.iterable[self.start - 1])

x = with_index(('apple', 'banana', 'cherry'))
print(list(x))


