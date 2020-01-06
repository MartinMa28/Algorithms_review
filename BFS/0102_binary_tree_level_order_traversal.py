from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        res = []
        
        if root:
            queue = deque([root])
            
            while queue:
                res.append([node.val for node in queue])
                next_level = []
                
                while queue:
                    popped = queue.popleft()

                    if popped.left:
                        next_level.append(popped.left)

                    if popped.right:
                        next_level.append(popped.right)
                
                queue = deque(next_level)
                
        return res