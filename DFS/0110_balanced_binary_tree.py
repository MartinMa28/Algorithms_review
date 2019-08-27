class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _check(self, root):
        if root == None:
            return (0, True)
        else:
            l_dep, l_balanc = self._check(root.left)
            r_dep, r_balanc = self._check(root.right)

            cur_dep = max(l_dep, r_dep) + 1
            is_balanc = l_balanc and r_balanc and abs(l_dep - r_dep) <= 1

            return cur_dep, is_balanc

    def isBalanced(self, root):
        return self._check(root)[1]
