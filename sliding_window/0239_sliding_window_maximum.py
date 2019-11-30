from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.queue = deque()
        
    def push(self, val):
        while len(self.queue) > 0 and self.queue[-1] < val:
            self.queue.pop()
            
        self.queue.append(val)
        
    def pop_left(self):
        self.queue.popleft()
        
    def get_max(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if len(nums) == 0 or k == 0:
            return []
        
        if k == 1:
            return nums
        
        ans = []
        mono_q = MonotonicQueue()
        
        for i in range(k):
            mono_q.push(nums[i])
        
        ans.append(mono_q.get_max())
        for i in range(k, len(nums)):
            if nums[i - k] == mono_q.get_max():
                mono_q.pop_left()
                
            mono_q.push(nums[i])
            
            ans.append(mono_q.get_max())
            
        return ans