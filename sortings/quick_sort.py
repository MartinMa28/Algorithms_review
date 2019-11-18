def quick_sort(nums):
    if nums == []:
        return

    pivot_idx = _partition(nums)

    quick_sort(nums[:pivot_idx])
    quick_sort(nums[pivot_idx + 1:])


def _partition(nums):
    pivot = nums[0]
    i = 0
    j = 1

    while j < len(nums):
        if nums[j] > pivot:
            j += 1
        else:
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
            j += 1

    nums[i], nums[0] = nums[0], nums[i]

    return i

    
if __name__ == "__main__":
    l = [5, 1, 3, 11, -9, 66]
    print(l)
    quick_sort(l)
    print(l)