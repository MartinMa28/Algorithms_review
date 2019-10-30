class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root == None:
            return float('inf')
        
        diff = target - root.val
        if diff > 0:
            sub_closest = self.closestValue(root.right, target)
        elif diff < 0:
            sub_closest = self.closestValue(root.left, target)
        else:
            return root.val
        
        
        if abs(root.val - target) > abs(sub_closest - target):
            return sub_closest
        else:
            return root.val