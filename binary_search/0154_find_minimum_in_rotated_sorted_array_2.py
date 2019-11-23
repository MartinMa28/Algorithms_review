class Solution:
    def findMin(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + ((right - left) >> 1)
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
                
        return nums[left]


if __name__ == "__main__":
    solu = Solution()
    print(solu.findMin([2, 2, 2, 0, 1]))