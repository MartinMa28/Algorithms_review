def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = (0 + len(nums)) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge_iterative(left, right)

def merge_iterative(nums1, nums2):
    if nums1 == []:
        return nums2
    
    if nums2 == []:
        return nums1

    i = 0 # for nums1
    j = 0 # for nums2

    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1


    if i < len(nums1):
        res += nums1[i:]
    else:
        res += nums2[j:]

    return res

    
def merge(nums1, nums2):
    if nums1 == []:
        return nums2
    
    if nums2 == []:
        return nums1

    if nums1[0] < nums2[0]:
        return [nums1[0]] + merge(nums1[1:], nums2)
    else:
        return [nums2[0]] + merge(nums1, nums2[1:])

if __name__ == "__main__":
    test = [99, -18, -1, 90, 98, 6]
    print(merge_sort(test))

    