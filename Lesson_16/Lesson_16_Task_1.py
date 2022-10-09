class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f'{self.fname} {self.lname}')

class Teacher(Person):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def your_salary(self):
        print(f'{self.fname} {self.lname} your salary is {self.salary}')

class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self.grade = grade

    def welcome(self):
        print(f"Welcome {self.fname} {self.lname} to the {self.grade} grade")

s = Student('Tony', 'Kava', '11FM')
s.welcome()
s.printname()
t = Teacher('Carl', 'Johnson', 'Ah shit... Here we go again, + reputation + 400$')
t.printname()
t.your_salary()


