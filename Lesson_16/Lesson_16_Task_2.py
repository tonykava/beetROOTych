class Mathematician:

    def square_nums(self, l1st):
        self.l1st = l1st
        return [i ** 2 for i in self.l1st]

    def remove_positives(self, l1st):
        self.l1st = l1st
        return [i for i in self.l1st if i < 0]

    def filter_leaps(self, l1st):
        self.l1st = l1st
        return [i for i in self.l1st if i % 4 == 0]

m = Mathematician()

print(m.square_nums([7, 11, 5, 6]))
print(m.remove_positives([23, 34, -34, 1, -768, -23]))
print(m.filter_leaps([2000, 2001, 2004, 2005, 2010]))