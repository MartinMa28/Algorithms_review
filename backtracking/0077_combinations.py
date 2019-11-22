class Solution:
    def __init__(self):
        self.res = []
    
    def _backtrack(self, nums, length, cur_com):
        if len(cur_com) == length:
            self.res.append(cur_com[:])
            
        for idx, n in enumerate(nums):
            if length - len(cur_com) <= len(nums) - idx:
                cur_com.append(n)
                self._backtrack(nums[idx + 1:], length, cur_com)

                # backtracking
                cur_com.pop()
        
                    
    def combine(self, n: int, k: int) -> list:
        nums = list(range(1, n + 1))
        
        self._backtrack(nums, k, [])
        
        return self.res


if __name__ == "__main__":
    solu = Solution()
    print(solu.combine(5, 2))