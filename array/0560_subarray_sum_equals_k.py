class Solution:
    
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0
#         for i in range(len(nums)):
#             cumulative = 0
#             for j in range(i, len(nums)):
#                 cumulative += nums[j]
                
#                 if cumulative == k:
#                     res += 1
                    
#         return res
    
    def subarraySum(self, nums: list, k: int) -> int:
        
        res = 0
        cumulative = 0
        sum_to_cnt = {0: 1}
        
        for n in nums:
            cumulative += n
            res += sum_to_cnt.get(cumulative - k, 0)
            
            if cumulative not in sum_to_cnt:
                sum_to_cnt[cumulative] = 1
            else:
                sum_to_cnt[cumulative] += 1
            
            
            
        return res
                
        