from stack import Stack


def fun(exp):
    s = Stack()

    for i in exp:
        if i in '({[':
            s.push(i)
        else:
            if s.is_empty():
                return False
            current = s.pop()
            if current == '(' and i != ')':
                return False
            if current == '[' and i != ']':
                return False
            if current == '{' and i != '}':
                return False

    return s.is_empty()


print(fun("{()}[]"))
print(fun(')}['))





