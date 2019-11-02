def binary_search(nums, left, right, target):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, left, mid - 1, target)
        else:
            return binary_search(nums, mid + 1, right, target)

def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 6, 9, 10, 99, 101]

    print(binary_search_iterative(nums, 19))
    