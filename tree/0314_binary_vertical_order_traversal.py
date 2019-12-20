from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.node_col = {}
        self.left_most = float('inf')
        self.right_most = -float('inf')
        
        
    def _recursive(self, root: TreeNode, idx: int) -> None:
        if root:
            self.node_col[root] = idx
            self.left_most = min((self.left_most, idx))
            self.right_most = max((self.right_most, idx))
            
            self._recursive(root.left, idx - 1)
            self._recursive(root.right, idx + 1)
        
    
    def verticalOrder(self, root: TreeNode) -> list:
        if root == None:
            return []
        
        self._recursive(root, 0)
        vertical_trav = [[] for _ in range(self.left_most, self.right_most + 1)]
        
        # level-order traverse
        queue = deque([root])
        
        while len(queue) > 0:
            popped = queue.popleft()
            vertical_trav[self.node_col[popped] + abs(self.left_most)].append(popped.val)
            
            if popped.left:
                queue.append(popped.left)
                
            if popped.right:
                queue.append(popped.right)
                
        return vertical_trav