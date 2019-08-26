def insertion_sort(nums):
    # In the i-th iteration, bubble the i-th element (the first element in the unsorted part)
    # until it reaches the right spot in the sorted section.
    length = len(nums)

    for i in range(1, length):
        ele_idx = i
        for j in range(i - 1, -1, -1):
            if nums[ele_idx] > nums[j]:
                break
            else:
                nums[ele_idx], nums[j] = nums[j], nums[ele_idx]
                ele_idx = j
    
    return nums


if __name__ == '__main__':
    unsorted = [2, 7, 4, 1, 5, 3]
    print(insertion_sort(unsorted))

