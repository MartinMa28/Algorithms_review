class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # slower keeps track of the unique part of the array
        # faster check if there is a new value in the next position
        
        if len(nums) == 1:
            return 1
        
        slower = 0
        faster = slower + 1

        while faster < len(nums):
            if nums[slower] != nums[faster]:
                slower += 1
                nums[slower] = nums[faster]
            
            faster += 1
        
        return slower + 1


if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]

    print(solu.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


        