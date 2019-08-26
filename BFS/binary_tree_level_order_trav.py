class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _max_height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return max(self._max_height(root.left), self._max_height(root.right)) + 1

    def levelOrder(self, root: TreeNode) -> list:
        queue = []
        h = self._max_height(root)
        traversal = [[] for _ in range(h)]

        if root == None:
            return []

        queue.append((root, 0))

        while len(queue):
            node, level = queue.pop(0)
            traversal[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return traversal