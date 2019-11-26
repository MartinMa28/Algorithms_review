class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}
    
    def _rob(self, root, rob) -> int:
        if (root, rob) in self.memo:
            return self.memo[(root, rob)]
        
        if root == None:
            self.memo[(root, rob)] = 0
            return 0
        elif root.left == None and root.right == None:
            if rob:
                self.memo[(root, rob)] = root.val
                return root.val
            else:
                self.memo[(root, rob)] = 0
                return 0
        else:
            if rob:
                profit = max((root.val + self._rob(root.left, False) + self._rob(root.right, False), self._rob(root.left, True) + self._rob(root.right, True)))
                self.memo[(root, rob)] = profit
                return profit
            else:
                profit = self._rob(root.left, True) + self._rob(root.right, True)
                self.memo[(root, rob)] = profit
                return profit
    
    def rob(self, root: TreeNode) -> int:
        return max((self._rob(root, False), self._rob(root, True)))