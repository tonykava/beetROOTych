def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return False



arr = [1, 3, 5, 7, 9, 11]

print(binary_search(arr, 0, len(arr)-1, 5))

