class Node:
    def __init__(self, x, children):
        self.val = x
        self.children = children

class Solution:
    def maxDepth(self, root: Node) -> int:
        if root == None:
            return 0
        
        if root.children == []:
            return 1

        max_subtree_depth = max(map(self.maxDepth, root.children))

        return max_subtree_depth + 1
