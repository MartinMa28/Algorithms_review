class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []


    def _inorder_trav(self, root: TreeNode) -> None:
        if root:
            self._inorder_trav(root.left)
            self.trav.append(root.val)
            self._inorder_trav(root.right)


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self._inorder_trav(root)
        res = self.trav[k - 1]
        self.trav = []

        return res