class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        h_m = dict(zip(nums, range(len(nums))))

        for idx, n in enumerate(nums):
            diff = target - n
            if diff in h_m and idx != h_m[diff]:
                return idx, h_m[diff]

    
    def twoSum_onepass(self, nums: list, target: int) -> list:
        h_m = {}

        for idx, n in enumerate(nums):
            diff = target - n
            if h_m.get(diff) is not None:
                return h_m.get(diff), idx
            else:
                h_m[n] = idx


if __name__ == "__main__":
    solu = Solution()
    solu.twoSum_onepass([2,7,11,15], 9)