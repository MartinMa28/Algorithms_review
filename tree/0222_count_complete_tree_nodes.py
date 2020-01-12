class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _depth(self, root):
        if not root:
            return 0
        else:
            return self._depth(root.left) + 1
        
    def _exist(self, idx, depth, node):
        left = 1
        right = 2 ** depth
        
        for _ in range(depth):
            mid = (left + right) // 2
            if idx > mid:
                left = mid + 1
                node = node.right
            else:
                right = mid
                node = node.left
        
        return node
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = self._depth(root) - 1
        
        left = 1
        right = 2 ** depth
        for _ in range(depth):
            mid = (left + right) // 2 + ((left + right) % 2)
            if self._exist(mid, depth, root):
                left = mid
            else:
                right = mid - 1
             
        return (2 ** depth - 1) + left