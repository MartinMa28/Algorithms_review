def bubble_sort(nums):
    length = len(nums)
    for i in range(0, length - 1):
        # In the i-th iter, the last i-th elements are sorted.
        for j in range(0, length - 1 - i):
            if nums[j] > nums[j + 1]:
                # In the unsorted part, swap the adjacent pair of elements 
                # if they are not in the right order.
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums


if __name__ == '__main__':
    unsorted = [2, 7, 4, 1, 5, 3]
    print(bubble_sort(unsorted))