from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    
    def _preorder(self, root):
        if root:
            if root.left:
                self.graph[root].append(root.left)
                self.graph[root.left].append(root)
                self._preorder(root.left)
            if root.right:
                self.graph[root].append(root.right)
                self.graph[root.right].append(root)
                self._preorder(root.right)
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> list:
        # build an adjacent list to represent the graph
        self._preorder(root)
        queue = deque()
        queue.append((target, 0))
        visited = set([target])
        
        res = []
        while len(queue) > 0:
            popped, dist = queue.popleft()
            
            if dist == K:
                res.append(popped.val)
            elif dist > K:
                break
                
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return res