# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def _left_most_node(self, root: 'TreeNode') -> 'TreeNode':
        if root:
            left_most = root
            
            while left_most.left:
                left_most = left_most.left
            
            return left_most
        else:
            return root
    
    def inorderSuccessor_recursive(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        if root.val < p.val:
            recursively find the successor on right sub tree
        elif root.val == p.val:
            return the left-most node on the right sub tree
        else:
            recursively find the successor on left sub tree,
            if the result on left sub tree is empty:
                return current node
            otherwise:
                return the result from recusion
        """
        if root.val < p.val:
            return self.inorderSuccessor(root.right, p)
        elif root is p:
            return self._left_most_node(root.right)
        else:
            res = self.inorderSuccessor(root.left, p)
            if res:
                return res
            else:
                return root

    
    def inorderSuccessor_iterative(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = [root]
        visited = set()
        successor = None
        found_p = False
        
        
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
                continue
            else:
                if found_p:
                    successor = stack.pop()
                    break
                else:
                    popped = stack.pop()
                    visited.add(popped)
                    if popped is p:
                        found_p = True
                        
                    if popped.right:
                        stack.append(popped.right)
                        
        return successor