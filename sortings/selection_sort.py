def selection_sort(nums):
    # In i-th iter, find the smallest element in the unsorted part
    # and swap the smallest element with the element in the i-th position.
    length = len(nums)
    for i in range(0, length - 1):
        min_idx = i

        for j in range(i + 1, length):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        temp = nums[i]
        nums[i] = nums[min_idx]
        nums[min_idx] = temp

    return nums


if __name__ == '__main__':
    unsorted = [2, 7, 4, 1, 5, 3]
    print(selection_sort(unsorted))