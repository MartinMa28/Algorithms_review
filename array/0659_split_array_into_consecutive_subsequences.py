from collections import defaultdict

class Solution:
    
    def isPossible(self, nums: list) -> bool:
        n_cnt = defaultdict(int)
        h_m = defaultdict(int)
        
        for n in nums:
            n_cnt[n] += 1
        
        
        for n in nums:
            if n_cnt[n] == 0:
                continue
            elif h_m[n] > 0:
                h_m[n] -= 1
                h_m[n + 1] += 1
                n_cnt[n] -= 1
            elif n_cnt[n + 1] > 0 and n_cnt[n + 2] > 0:
                n_cnt[n + 1] -= 1
                n_cnt[n + 2] -= 1
                n_cnt[n] -= 1
                h_m[n + 3] += 1
            else:
                return False
        
        return True