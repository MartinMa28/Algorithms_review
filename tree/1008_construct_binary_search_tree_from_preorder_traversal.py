from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _build_tree(self, preorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root_val = preorder.popleft()
        root = TreeNode(root_val)
        
        left = deque(filter(lambda x: x < root_val, preorder))
        right = deque(filter(lambda x: x > root_val, preorder))
        
        root.left = self._build_tree(left)
        root.right = self._build_tree(right)
        
        return root
    
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        preorder = deque(preorder)
        
        return self._build_tree(preorder)