class Solution:
    def __init__(self):
        self.res = []
    
    def _backtrack(self, nums, cur_perm):
        if nums == []:
            self.res.append(cur_perm[:])
            
        for idx, n in enumerate(nums):
            cur_perm.append(n)
            self._backtrack(nums[:idx] + nums[idx + 1:], cur_perm)
            
            # backtracking
            cur_perm.pop()
    
    def permute(self, nums: list) -> list:
        self._backtrack(nums, [])
        
        return self.res


if __name__ == "__main__":
    solu = Solution()
    print(solu.permute([1, 2, 3, 4]))
