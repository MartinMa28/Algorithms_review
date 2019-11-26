# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []
        
    def _is_leaf(self, root):
        return root.left == None and root.right == None
        
    def _remove_one_layer(self, root):
        if root == None:
            return root
        
        if self._is_leaf(root):
            self.res.append(root.val)
            return None
        
        root.left = self._remove_one_layer(root.left)
        root.right = self._remove_one_layer(root.right)
        
        return root
        
        
    
    def findLeaves_top_down(self, root: TreeNode) -> list:
        results = []
        while root:
            self.res = []
            root = self._remove_one_layer(root)
            results.append(self.res[:])
            
        return results 
    
    
    def _dfs(self, root):
        if root == None:
            return 0
        
        left_level = self._dfs(root.left)
        right_level = self._dfs(root.right)
        level = max((left_level, right_level)) + 1
        
        if len(self.res) < level:
            self.res.append([root.val])
        else:
            self.res[level - 1].append(root.val)
        
        return level
    
    def findLeaves(self, root: TreeNode) -> list:
        self._dfs(root)
        
        return self.res