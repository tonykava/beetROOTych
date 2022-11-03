from Task_1 import Node
from Task_1 import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.items.size == 0

    def push(self, item):
        self.items.add(item)

    def pop(self):
        self.items.pop(0)

    def __repr__(self):
        next_n = self.items.head
        result = ''

        while next_n:
            result += str(next_n.data) + ' -> '
            next_n = next_n.next_node
        return result

    def peek(self):
        return self.items.index(self.items.size - 1)


    def size(self):
        return self.items.size


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    s.pop()
    print(s)
    print(s.peek())
    print(s.size())
    print(s.is_empty())





