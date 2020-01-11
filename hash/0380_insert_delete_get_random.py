import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_idx = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.nums_idx:
            return False
        else:
            self.nums_idx[val] = len(self.nums)
            self.nums.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.nums:
            return False
        else:
            if val == self.nums[-1]:
                self.nums.pop()
                self.nums_idx.pop(val)
            else:
                self.nums[self.nums_idx[val]] = self.nums[-1]
                self.nums_idx[self.nums[-1]] = self.nums_idx[val]
                self.nums.pop()
                self.nums_idx.pop(val)
                
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()