def quick_sort(nums, start, end):
    if nums == []:
        return

    if start >= end:
        return

    pivot_idx = _partition(nums, start, end)

    quick_sort(nums, start, pivot_idx - 1)
    quick_sort(nums, pivot_idx + 1, end)


def _partition(nums, start, end):
    pivot = nums[start]
    i = start
    j = start + 1

    while j < len(nums):
        if nums[j] > pivot:
            j += 1
        else:
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            i += 1
            j += 1

    nums[i], nums[start] = nums[start], nums[i]

    return i

    
if __name__ == "__main__":
    l = [12, -4, 5, 6, -1, 9, 4, -3, 7]
    print(l)
    quick_sort(l, 0, len(l) - 1)
    print(l)