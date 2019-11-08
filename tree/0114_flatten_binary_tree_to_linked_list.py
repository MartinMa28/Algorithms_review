# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        
        stack = [root]
        
        prev = TreeNode(-1)
        head = prev
        while len(stack) > 0:
            popped = stack.pop()
            
            if popped.right:
                stack.append(popped.right)
            
            if popped.left:
                stack.append(popped.left)
                
            popped.left = None
            popped.right = None
            prev.right = popped
            prev = popped
            
        return head.right