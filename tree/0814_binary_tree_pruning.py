# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        bottom-up:
        cur.left = prune(cur.left)
        cur.right = prune(cur.right)
        
        if (not cur_left) and (not cur_right) and cur.val == 0:
            return None
        else:
            return cur
        
        """
        if root == None:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if (not root.left) and (not root.right) and root.val == 0:
            # If both of the left and right sub-tree don't contain 1,
            # and the current node is 0, the root node should be pruned.
            return None
        else:
            return root