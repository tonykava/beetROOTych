from random import randint
def oops(a):
    arr = [i for i in range(a)]
    return arr[a + 2]


def try_oops():
    try:
        return oops(randint(1, 100))
    except IndexError:
        print('Your index out of range')


print(try_oops())

# Якщо в блоці: "try/except" замінити IndexError на KeyError - тоді блок не буде відловлювати помилку перевищення індексу.
