class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
    
    def _backtrack(self, root, cur_path):
        cur_path.append(root.val)
        if root.left == None and root.right == None:
            # root is a leaf node
            if sum(cur_path) == self.target:
                self.res.append(cur_path[:])
        
        if root.left:
            self._backtrack(root.left, cur_path)
        
        if root.right:
            self._backtrack(root.right, cur_path)

        # backtrack
        cur_path.pop()
            
    
    def pathSum(self, root: TreeNode, s: int) -> list:
        if root == None:
            return []
        
        self.target = s
        self._backtrack(root, [])
        
        return self.res