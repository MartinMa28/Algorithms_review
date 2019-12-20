class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _is_same(self, s: TreeNode, t: TreeNode) -> bool:
        if s and t:
            if s.val == t.val and \
                self._is_same(s.left, t.left) and \
                self._is_same(s.right, t.right):
                return True
        elif s == None and t == None:
            return True
        else:
            return False
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            if t == None:
                return True
            else:
                return False
            
        if self._is_same(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)