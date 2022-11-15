class BinaryHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def insert(self, k):
        self.heaplist.append(k)
        self.currentsize += 1
        self.percup(self.currentsize)

    def percup(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def maxchild(self, i):
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] > self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percdown(self, i):
        while (i * 2) <= self.currentsize:
            mc = self.maxchild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def delmax(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize -= 1
        self.heaplist.pop()
        self.percdown(1)
        return retval

    def buildheap(self, arr):
        i = len(arr) // 2
        self.currentsize = len(arr)
        self.heaplist = [0] +arr[:]
        while (i > 0):
            self.percdown(i)
            i = i - 1

class PriorityQueue:
    def __init__(self, arr):
        self.arr = arr
        self.pq = BinaryHeap()
        self.pq.buildheap(self.arr)

    def dequeue(self):
        return self.pq.delmax()

    def enqueue(self, i):
        self.pq.insert(i)


if __name__ == '__main__':
    p = PriorityQueue([9, 5, 6, 2, 3])
    p.enqueue(100000)
    p.enqueue(1212)
    print(p.dequeue())
    print(p.dequeue())






