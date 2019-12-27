class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        if not nums1 or not nums2:
            return []
        
        next_greater = {}
        i = 1
        # monotonous stack following an ascending order from top to bottom
        mono_stack = [nums2[0]]
        
        for num in nums2[1:]:
            while mono_stack:
                if num > mono_stack[-1]:
                    next_greater[mono_stack.pop()] = num
                else:
                    break
            
            mono_stack.append(num)
            
            
        
        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            if n in next_greater:
                res[i] = next_greater[n]
                
        return res