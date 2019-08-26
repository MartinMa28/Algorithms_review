class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []

    def _postorder_traversal_recursive(self, root: TreeNode) -> None:
        if root:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            self.trav.append(root.val)

    def _postorder_traversal(self, root: TreeNode) -> list:
        stack = []
        traversal = []

        if root == None:
            return []

        # Postorder traversal is equal to the reversed "root, right, left" traversal, which
        # is a variation of preorder traversal
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            traversal.append(node.val)
            # Traverse following the order of root, right and left, so push left before right child.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # reverse traversal
        for i in range(len(traversal) // 2):
            traversal[i], traversal[len(traversal) - 1 - i]  = traversal[len(traversal) - 1 - i], traversal[i]

        return traversal


    def postorderTraversal(self, root: TreeNode) -> None:
        self._postorder_traversal(root)
        traversal = self.trav
        self.trav = []

        return traversal