class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.found = False
    
    def _dfs(self, root, given_sum, cur_sum=0):
        if root.left == None and root.right == None:
            if cur_sum + root.val == given_sum:
                self.found = True
                return
            else:
                return
        
        if root.left:
            self._dfs(root.left, given_sum, cur_sum + root.val)
            if self.found:
                return
        
        if root.right:
            self._dfs(root.right, given_sum, cur_sum + root.val)
            if self.found:
                return
        
        
    
    def hasPathSum(self, root: TreeNode, given_sum: int) -> bool:
        if root == None:
            return False
        
        if self._is_leaf(root):
            if root.val == given_sum:
                return True
            else:
                return False
            
        return self.hasPathSum(root.left, given_sum - root.val) or self.hasPathSum(root.right, given_sum - root.val)

    
    def _is_leaf(self, node):
        return node.left is None and node.right is None
    
    def hasPathSum_iterative(self, root: TreeNode, given_sum: int) -> bool:
        if root == None:
            return False
        
        stack = [(root, given_sum - root.val)]
        
        while len(stack) > 0:
            popped, left_sum = stack.pop()
            
            if self._is_leaf(popped):
                if left_sum == 0:
                    return True
            else:
                if popped.right:
                    stack.append((popped.right, left_sum - popped.right.val))
                
                if popped.left:
                    stack.append((popped.left, left_sum - popped.left.val))
        
        return False