class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, element):
        self.element = element
        arr = []
        while not self.is_empty():
            current = self.pop()
            if current == element:
                for i in arr[::-1]:
                    s.push(i)
                return current
            else:
                arr.append(current)
        if self.is_empty():
            raise ValueError('There is no such element in our stack')


    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.get_from_stack(1))
    print(s)
