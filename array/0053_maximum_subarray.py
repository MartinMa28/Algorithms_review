class Solution:
    def _max_cross(self, nums: list, idx: int) -> int:
        max_subsum = -float('inf')

        cur_sum = 0
        # check the left side
        for i in range(idx, -1, -1):
            cur_sum += nums[i]
            if cur_sum > max_subsum:
                max_subsum = cur_sum
        
        left_max = max_subsum
        max_subsum = -float('inf')
        
        # check the right side
        cur_sum = 0
        for i in range(idx + 1, len(nums)):
            cur_sum += nums[i]
            if cur_sum > max_subsum:
                max_subsum = cur_sum

        right_max = max_subsum

        if right_max > 0:
            return right_max + left_max
        else:
            return left_max

    def maxSubArray_divide_conquer(self, nums: list) -> int:
        if len(nums) == 0:
            return -float('inf')
        elif len(nums) == 1:
            return nums[0]
        else:
            mid = len(nums) // 2
            max_left = self.maxSubArray(nums[:mid])
            max_right = self.maxSubArray(nums[mid + 1:])
            max_cross = self._max_cross(nums, mid)

            return max((max_left, max_cross, max_right))

    def maxSubArray(self, nums: list) -> int:
        cumu_sum = -float('inf')
        max_sum = -float('inf')

        for n in nums:
            cumu_sum += n
            
            if n > cumu_sum:
                # if a single number is larger than cumulative max,
                # stop cumulating further, let this number be the starting point
                cumu_sum = n

            if cumu_sum > max_sum:
                # update the max
                max_sum = cumu_sum

        return max_sum


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))