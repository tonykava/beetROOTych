class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f'Library name is {self.name}. Books: {[i.name for i in self.books]}. Authors: {[i.name for i in self.authors]}'

    def __repr__(self):
        return f'Library(name = {self.name}. Books: {[i.name for i in self.books]}. Authors: {[i.name for i in self.authors]}'

    def new_book(self, name, year, author):
        self.books.append(Book(name, year, author))
        if author not in self.authors:
            self.authors.append(author)
        Book.books_count += 1
        return Book(name, year, author)

    def group_by_author(self, author):
        print([i.name for i in self.books if i.author == author])

    def group_by_year(self, year):
        print([i.name for i in self.books if i.year == year])


class Book:
    books_count = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'Book name: {self.name}, Book year: {self.year}, Book author: {self.author}'
    def __repr__(self):
        return f'Book name: {self.name}, Book year: {self.year}, Book author: {self.author}'


class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'Authors name: {self.name}, Authors country: {self.country}, Authors birthday: {self.birthday}, Authors books: {self.books}'
    def __repr__(self):
        return f'Authors name: {self.name}, Authors country: {self.country}, Authors birthday: {self.birthday}, Authors books: {self.books}'


l = Library('MyLib')
a = Author('Stephen King', 'USA', '21.09.1947', ['Misery', 'The Green Mile', 'Doctor Sleep', 'Skeleton Crew', 'Desperation'])
a1 = Author('Andrzej Sapkowski', 'Poland', '21.06.1948', ['The Witcher', 'Sword of Destiny', 'The Last Wish'])

l.new_book('The Witcher', 1990, a1)
l.new_book('The Last Wish', 1993, a1)
l.new_book('Sword of Destiny', 1967, a1)
l.new_book('Misery', 1967, a)
l.new_book('The Green Mile', 1980, a)
l.group_by_author(a)
l.group_by_year(1967)
print(l.__str__())
print(l.__repr__())
print(a.__str__())
print(a1.__repr__())
print(l.books[1].__str__())
print(l.books[2].__repr__())
