class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []

    def _postorder_traversal(self, root: TreeNode) -> None:
        if root:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            self.trav.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> None:
        self._postorder_traversal(root)
        traversal = self.trav
        self.trav = []

        return traversal