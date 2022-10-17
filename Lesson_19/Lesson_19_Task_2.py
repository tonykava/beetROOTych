class in_range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            self.start += self.step
            return self.start - self.step

n = in_range(1, 10, 2)

print(list(n))



