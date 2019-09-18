class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if preorder == [] or inorder == []:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx + 1:])

        return root