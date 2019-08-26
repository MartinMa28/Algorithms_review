class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []

    def _preorder_traversal(self, root: TreeNode) -> None:
        if root:
            self.trav.append(root.val)
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)

    def preorderTraversal(self, root: TreeNode) -> list:
        self._preorder_traversal(root)
        traversal = self.trav
        self.trav = []

        return traversal
