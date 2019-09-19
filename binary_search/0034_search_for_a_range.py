class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if nums == []:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return [-1, -1]
        
        left_most = left

        left = 0
        right = len(nums) - 1

        while left < right:
            # instead of going floor, go ceil to get the right most
            mid = ((left + right) + ((left + right) % 2)) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1

        right_most = right

        return [left_most, right_most]       



if __name__ == "__main__":
    solu = Solution()
    print(solu.searchRange([5,7,7,8,10], 8))
    