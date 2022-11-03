from Task_1 import Node
from Task_1 import LinkedList

class Queue:
    def __init__(self):
        self.que = LinkedList()

    def is_empty(self):
        return self.que.size == 0

    def enqueue(self, item):
        self.que.add(item)

    def dequeue(self):
        self.que.pop(self.que.size - 1)


    def size(self):
        return self.que.size

    def __repr__(self):
        next_n = self.que.head
        result = ''

        while next_n:
            result += str(next_n.data) + ' -> '
            next_n = next_n.next_node
        return result

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    q.dequeue()
    print(q)
    print(q.size())
    q.enqueue(1)
    print(q)







