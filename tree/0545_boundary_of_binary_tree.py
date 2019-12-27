class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
                
    def _find_leaves(self, root, leaves):
        if not self._is_leaf(root):
            if root.left:
                self._find_leaves(root.left, leaves)
            
            if root.right:
                self._find_leaves(root.right, leaves)
        else:
            leaves.append(root.val)
    
    def _is_leaf(self, root):
        return root.left == None and root.right == None
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> list:
        res = []
        
        if not root:
            return res
        
        res = [root.val]
        if self._is_leaf(root):
            return res
        
        cur = root.left
        while cur:
            if not self._is_leaf(cur):
                res.append(cur.val)
            
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        self._find_leaves(root, res)
            
        stack = []
        cur = root.right
        while cur:
            if not self._is_leaf(cur):
                stack.append(cur.val)
            
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
                
        while stack:
            res.append(stack.pop())
        
        return res