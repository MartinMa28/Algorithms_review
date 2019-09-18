class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _build_tree(self, inorder: list, reversed_postorder: list) -> TreeNode:
        if reversed_postorder == [] or inorder == []:
            return None
        
        root_val = reversed_postorder.pop(0)
        root = TreeNode(root_val)
        root_idx = inorder.index(root_val)

        root.right = self._build_tree(inorder[root_idx + 1:], reversed_postorder)
        root.left = self._build_tree(inorder[:root_idx], reversed_postorder)

        return root
        

    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        reversed_postorder = reversed(postorder)

        return self._build_tree(inorder, reversed_postorder)
