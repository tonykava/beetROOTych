from stack import Stack


def reverse_seq(arr):

    s = Stack()
    for i in arr:
        s.push(i)
    print([s.pop() for i in range(len(arr))])


reverse_seq([0, 1, 2, 3])





