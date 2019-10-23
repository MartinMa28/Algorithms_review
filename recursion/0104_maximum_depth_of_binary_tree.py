class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0
    
    def maxDepth_bottom_up(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return max((self.maxDepth(root.left), self.maxDepth(root.right))) + 1
    
    
    def _top_down(self, root, cur_depth) -> None:
        if root == None:
            return
        else:
            if cur_depth > self.ans:
                self.ans = cur_depth

            self._top_down(root.left, cur_depth + 1)
            self._top_down(root.right, cur_depth + 1)
    
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self._top_down(root, 1)
        
        return self.ans