class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trav = []

    def _inorder_traversal_recursive(self, root: TreeNode) -> None:
        if root:
            self._inorder_traversal(root.left)
            self.trav.append(root.val)
            self._inorder_traversal(root.right)

    def _inorder_traversal(self, root: TreeNode) -> list:
        stack = []
        traversal = []
        stack.append(root)
        visited = []
        while len(stack) > 0:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
            else:
                popped = stack.pop()
                traversal.append(popped.val)
                visited.append(popped)
                if popped.right:
                    stack.append(popped.right)

        return traversal

    def inorderTraversal(self, root: TreeNode) -> list:
        self._inorder_traversal(root)
        traversal = self.trav
        self.trav = []
        return traversal


if __name__ == '__main__':
    solu = Solution()
    r = TreeNode(1)
    r_r = TreeNode(2)
    r_r_l = TreeNode(3)
    r.right = r_r
    r_r.left = r_r_l

    trav = solu._inorder_traversal(r)
    
    print(trav)

    