class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = 0
        nums.sort()
        max_val = nums[len(nums)-1] - nums[0]
        
        while min_val < max_val:
            mid = (max_val+min_val)//2
            cnt = self.countSmaller(nums, mid)
            if cnt<k:
                min_val = mid+1
            else:
                max_val = mid
        
        return min_val
    
    
    def countSmaller(self, nums, mid):
        count = 0
        j = 1
        for i in range(len(nums)):
            while j<len(nums) and nums[j]-nums[i]<=mid:
                j+=1
            count += (j-i-1)
            
        return count
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.countSmaller([1, 1, 3, 7], 2))