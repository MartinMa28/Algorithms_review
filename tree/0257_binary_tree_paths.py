# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.results = []
        
    def _dfs(self, root, cur_path):
        if root.left == None and root.right == None:
            cur_path += str(root.val)
            self.results.append(cur_path)
        else:
            if root.left:
                self._dfs(root.left, cur_path + str(root.val) + '->')
            if root.right:
                self._dfs(root.right, cur_path + str(root.val) + '->')
            
    
    def binaryTreePaths(self, root: TreeNode) -> list:
        if root == None:
            return []
        
        self._dfs(root, '')
        
        return self.results