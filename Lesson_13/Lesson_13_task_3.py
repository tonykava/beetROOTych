def choose_func(nums, func1, func2):
    if sum([1 for i in nums if i >= 0]) == len(nums):
        return func1
    else:
        return func2


# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


print(choose_func(nums1, square_nums(nums1), remove_negatives(nums1)))
print(choose_func(nums2, square_nums(nums2), remove_negatives(nums2)))
