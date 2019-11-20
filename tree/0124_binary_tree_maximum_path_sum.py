# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.max_sum = -float('inf')
    
    
    def _max_path_sum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self._max_path_sum(root.left)
        right = self._max_path_sum(root.right)
        
        self.max_sum = max((self.max_sum, left + root.val, right + root.val, root.val + left + right, root.val))
        
        if max((left, right)) > 0:
            return root.val + max((left, right))
        else:
            return root.val
        
    def maxPathSum(self, root: TreeNode) -> int:
        self._max_path_sum(root)
        
        return self.max_sum