class Solution:
    def findMin(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]


if __name__ == "__main__":
    solu = Solution()
    solu.findMin([4,5,6,0,1,2,3])
