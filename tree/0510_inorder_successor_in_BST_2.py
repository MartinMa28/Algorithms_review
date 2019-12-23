# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    
    def _left_most(self, node: 'Node') -> 'Node':
        if Node:
            left_most = node
            
            while left_most.left:
                left_most = left_most.left
                
            return left_most
        else:
            return node
    
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        """
        if the right subtree is not empty:
            return the left-most node in the right subtree
        else:
            find the closest parent that is greater than the node
            if cannot find such one, return None
        """
        
        if node.right:
            return self._left_most(node.right)
        else:
            parent = node.parent
            while parent:
                if parent.val > node.val:
                    return parent
                else:
                    parent = parent.parent
            
            return None