class Solution:
    def _binary_search(self, nums, left, right, val):
        """
        both of left and right is included index
        """
        if left > right:
            return None
        else:
            mid = (left + right) // 2
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                return self._binary_search(nums, left, mid - 1, val)
            else:
                return self._binary_search(nums, mid + 1, right, val)

    def twoSum(self, numbers: list, target: int) -> list:
        for li in range(0, len(numbers) - 1):
            diff = target - numbers[li]
            found_idx = self._binary_search(numbers, li + 1, len(numbers) - 1, diff)
            if found_idx:
                return [li + 1, found_idx + 1]


    def twoSum_two_pointers(self, numbers: list, target: int) -> list:
        left, right = 0, len(numbers) - 1

        while left <= right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

if __name__ == "__main__":
    solu = Solution()
    print(solu.twoSum_two_pointers([3,24,50,79,88,150,345], 200))