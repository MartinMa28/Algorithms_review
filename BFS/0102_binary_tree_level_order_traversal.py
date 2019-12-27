from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        else:
            res = []
            queue = deque([root])
            
            while len(queue) > 0:
                level = []
                next_level = []
                while len(queue) > 0:
                    popped = queue.popleft()
                    level.append(popped.val)
                    
                    if popped.left:
                        next_level.append(popped.left)
                    
                    if popped.right:
                        next_level.append(popped.right)
                        
                res.append(level)
                queue = deque(next_level)
                
            return res