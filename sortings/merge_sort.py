def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid_idx = len(nums) // 2
    left = merge_sort(nums[:mid_idx])
    right = merge_sort(nums[mid_idx:])

    return merge_recursive(left, right)

def merge_recursive(nums1, nums2):
    if nums1 == []:
        return nums2
    
    if nums2 == []:
        return nums1

    if nums1[0] < nums2[0]:
        return [nums1[0]] + merge_recursive(nums1[1:], nums2)
    else:
        return [nums2[0]] + merge_recursive(nums1, nums2[1:])

def merge(nums1, nums2):
    # merge 2 sorted arrays
    if len(nums1) == 0:
        return nums2
    
    if len(nums2) == 0:
        return nums1
    
    i = 0
    j = 0
    merged = []

    while True:
        if i == len(nums1):
            return merged + nums2[j:]
        
        if j == len(nums2):
            return merged + nums1[i:]
        
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1


if __name__ == '__main__':
    unsorted = [2, 7, 4, 1, 5, 3]
    print(merge_sort(unsorted))