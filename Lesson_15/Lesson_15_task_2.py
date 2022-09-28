class Dog:
    def __init__(self, dog_age):
        self.age_factor = 7
        self.dog_age = dog_age

    def human_age(self):
        print("Dog’s age in human equivalent: {}".format(self.age_factor * self.dog_age))

dog1 = Dog(3)

dog1.human_age()
