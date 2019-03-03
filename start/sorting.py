def switch_with_next(array, p):
    temp = array[p]
    array[p] = array[p+1]
    array[p+1] = temp


def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                switch_with_next(nums, j)


numbers = [1, 22, 4, 8, 2, 5, 3, 44, 6]


print(numbers)
bubble_sort(numbers)
print(numbers)
