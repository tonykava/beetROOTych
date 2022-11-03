class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def __repr__(self):
        next_n = self.head
        result = ''

        while next_n:
            result += str(next_n.data) + ' -> '
            next_n = next_n.next_node
        return result

    def remove(self, data):
        if self.size == 0:
            raise IndexError('pop from empty list')
        this_node = self.head
        prev_node = None

        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.head = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def append(self, data):
        new_node = Node(data)
        this_node = self.head
        if self.size == 0:
            self.add(data)
            self.size += 1
        else:
            while this_node.next_node:
                this_node = this_node.next_node
            this_node.next_node = new_node
            self.size += 1

    def index(self, id):
        this_node = self.head
        counter = 0
        while this_node:
            if counter == id:
                return this_node.data
            else:
                this_node = this_node.next_node
                counter += 1


    def pop(self, id):
        if self.size == 0:
            raise IndexError('pop from empty list')
        this_node = self.head
        counter = 0
        prev_node = None
        while this_node:
            if counter == id:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                    self.size -= 1
                    return this_node.data
                else:
                    self.head = this_node.next_node
                    self.size -= 1
                    return this_node.data
            else:
                counter += 1
                prev_node = this_node
                this_node = this_node.next_node

    def insert(self, data, id):
        new_node = Node(data)
        this_node = self.head
        counter = 0
        prev_node = None
        while this_node:
            if counter == id:
                if prev_node:
                    new_node.next_node = this_node
                    prev_node.next_node = new_node
                    self.size += 1
                    break
                else:
                    new_node = Node(data, self.head)
                    self.head = new_node
                    self.size += 1
                    break
            else:
                counter += 1
                prev_node = this_node
                this_node = this_node.next_node

    def slice(self, start, stop):
        arr = LinkedList()
        this_node = self.head
        counter = 0
        while counter < stop:
            if stop > counter >= start:
                arr.append(this_node.data)
                counter += 1
                this_node = this_node.next_node
            else:
                counter += 1
                this_node = this_node.next_node
        return arr

if __name__ == "__main__":
    l = LinkedList()
    l.add(5)
    l.add(9)
    l.add(7)
    print(l)
    l.remove(9)
    print(l)
    l.append(9)
    print(l)
    print(l.index(2))
    l.pop(1)
    print(l)
    l.insert(100, 1)
    print(l)
    l.insert(200, 0)
    print(l)
    print(l.slice(0, 3))







