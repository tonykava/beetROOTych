class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print("Hello, my name is {} {} and I'm {} years old".format(self.name, self.last_name, self.age))

p1 = Person('Carl', 'Johnson', 26)

p1.talk()
