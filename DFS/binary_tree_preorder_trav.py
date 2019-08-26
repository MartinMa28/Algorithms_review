class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []

    def _preorder_traversal_recursive(self, root: TreeNode) -> None:
        if root:
            self.trav.append(root.val)
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)

    def _preorder_traversal(self, root: TreeNode) -> list:
        stack = []
        traversal = []

        if root == None:
            return []
        
        stack.append(root)

        while len(stack) > 0:
            popped = stack.pop()
            traversal.append(popped.val)
            # Preorder traversal follows the order of root, left and right, so
            # push the right child before the left child into stack.
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)

        return traversal

    def preorderTraversal(self, root: TreeNode) -> list:
        self._preorder_traversal(root)
        traversal = self.trav
        self.trav = []

        return traversal
