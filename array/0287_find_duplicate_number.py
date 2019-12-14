class Solution:
    def findDuplicate(self, nums: list) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        start = nums[0]
        
        while start != slow:
            slow = nums[slow]
            start = nums[start]
            
        return start


if __name__ == "__main__":
    solu = Solution()
    print(solu.findDuplicate([1, 3, 4, 2, 2]))