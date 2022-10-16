class Boss:
    all_bosses = []

    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.workers = []
        self.new_boss()

    def new_boss(self):
        self.all_bosses.append(self)

    @property
    def all_workers(self):
        return [i.name for i in self.workers]


class Worker:
    def __init__(self, name, company):
        self.name = name
        self._company = company
        self._boss = None

    @property
    def chef(self):
        '''Get the current boss'''
        return self._boss

    @chef.setter
    def chef(self, value):
        for i in Boss.all_bosses:
            if i == value:
                self._boss = i
                self._company = i.company
                i.workers.append(self)
                break


w = Worker('Richard Hendrix', None)
w1 = Worker('Gilfoyle', None)

b = Boss('Gavin Belson', 'Hooli')
b1 = Boss('Lory Brim', 'Roviga')

w.chef = b
print(w.chef.name)
print(w.chef.company)
print('-----------------------')
w.chef = b1
print(w.chef.name)
print(w.chef.company)
w1.chef = b1
print(b1.all_workers)








