class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left)\
                    and self.isSameTree(p.right, q.right)
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False