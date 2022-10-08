class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def talk(self):
        print('Woof woof')

class Cat(Animal):
    def talk(self):
        print('meow meow')

d = Dog()
c = Cat()

for i in c, d:
    i.talk()

