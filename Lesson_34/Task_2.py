def merge(arr, start, mid, end):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    while (start <= mid and start2 <= end):

        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value
            start += 1
            mid += 1
            start2 += 1

def mergeSort(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

        return arr

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)

    print(mergeSort(arr, 0, arr_size - 1))

