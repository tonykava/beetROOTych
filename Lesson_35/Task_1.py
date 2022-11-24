def double_bubble(arr):

    n = len(arr)
    flag = True
    start = 0
    end = n - 1

    while flag:
        flag = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True

        if not flag:
            break

        flag = False
        end -= 1

        for i in range(end, start - 1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True

        start += 1

    return arr

if __name__ == '__main__':
    a = [5, 1, 4, 2, 8, 0, 2]
    double_bubble(a)
    print(a)
