class Solution:
    def _two_sum(self, nums: list, target: int) -> list:
        met = set()
        res = []
        for n in nums:
            diff = target - n
            if diff in met:
                if [diff, n] not in res:
                    res.append([diff, n])
            else:
                met.add(n)

        return res

    def threeSum(self, nums: list) -> list:
        solutions = set()
        for idx, n in enumerate(nums):
            res = self._two_sum(nums[0: idx] + nums[idx + 1:], -1 * n)
            
            for r in res:
                r.append(n)
                tup_r = tuple(sorted(r))
                if tup_r not in solutions:
                    solutions.add(tup_r)
        

        return [list(s) for s in solutions]
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))