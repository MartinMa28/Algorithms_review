class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        if not nums:
            return []
        
        monotonic_stack = [(nums[0], 0)]
        nums = nums + nums
        next_greater = {}
        
        for i, num in enumerate(nums[1:], 1):
            while monotonic_stack:
                if num > monotonic_stack[-1][0]:
                    val, idx = monotonic_stack.pop()
                    next_greater[(val, idx)] = num
                else:
                    break
            
            if i < len(nums) // 2:
                monotonic_stack.append((num, i))
            
        
        res = [-1] * (len(nums) // 2)
        
        for i, n in enumerate(nums[:len(nums) // 2]):
            if (n, i) in next_greater:
                res[i] = next_greater[(n, i)]
                
        return res