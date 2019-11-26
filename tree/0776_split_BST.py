# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> list:
        if root == None:
            return [None, None]
        
        if root.val <= V:
            sub_left, sub_right = self.splitBST(root.right, V)
            root.right = sub_left
            
            return [root, sub_right]
        else:
            sub_left, sub_right = self.splitBST(root.left, V)
            root.left = sub_right
            
            return [sub_left, root]