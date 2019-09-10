from collections import Counter

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
class Solution:
    def __init__(self):
        self.subtree_counter = Counter()
        self.ans = []

    def _dfs_preorder(self, root: TreeNode) -> str:
        if root == None:
            return '#'

        enc = '{}, {}, {}'.format(root.val, 
        self._dfs_preorder(root.left), 
        self._dfs_preorder(root.right))

        self.subtree_counter[enc] += 1
        if self.subtree_counter[enc] == 2:
            self.ans.append(root)

        return enc


    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        self._dfs_preorder(root)

        return self.ans

