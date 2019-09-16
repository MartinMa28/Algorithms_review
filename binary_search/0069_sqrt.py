class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        nums = range(1, x + 1)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] ** 2 == x:
                return nums[mid]
            elif nums[mid] ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1

        return nums[right]


if __name__ == "__main__":
    solu = Solution()

    print(solu.mySqrt(16))