# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _balance(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self._balance(root.left)
        right = self._balance(root.right)
        
        self.ans += abs(left) + abs(right)
        
        return root.val - 1 + left + right
    
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        
        self._balance(root)
        
        return self.ans