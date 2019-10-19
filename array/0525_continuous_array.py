class Solution:
    def findMaxLength(self, nums: list) -> int:
        cache = {0: 0}
        
        max_len = 0
        cnt = 0
        for idx, n in enumerate(nums, 1):
            if n == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt not in cache:
                cache[cnt] = idx
            else:
                max_len = max((max_len, idx - cache[cnt]))
        
        return max_len

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMaxLength([0, 1]))