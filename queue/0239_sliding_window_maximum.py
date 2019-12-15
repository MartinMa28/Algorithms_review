from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.mono_q = deque()
        
    def push(self, x):
        while len(self.mono_q) > 0 and self.mono_q[-1] < x:
            self.mono_q.pop()
            
        self.mono_q.append(x)
        
    def popleft(self):
        return self.mono_q.popleft()
    
    def get_max(self):
        return self.mono_q[0]
    
    def __len__(self):
        return len(self.mono_q)
    
    def __str__(self):
        return str(self.mono_q)
        
    

class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if nums == [] and k == 0:
            return nums
        
        if k == 1:
            return nums
        
        mono_q = MonotonicQueue()
        for i in range(k):
            mono_q.push(nums[i])
            
        res = [mono_q.get_max()]
        
        for i in range(1, len(nums) - k + 1):
            if len(mono_q) > 0 and nums[i - 1] == mono_q.get_max():
                mono_q.popleft()
            
            mono_q.push(nums[i + k - 1])
            res.append(mono_q.get_max())
            
        return res