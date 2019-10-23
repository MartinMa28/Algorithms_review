# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _is_mirror(self, left, right):
        if left == None and right == None:
            return True
        elif (left == None and right) or (left and right == None):
            return False
        else:
            return left.val == right.val and self._is_mirror(left.left, right.right) and self._is_mirror(left.right, right.left)
    
    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self._is_mirror(root.left, root.right)

                

