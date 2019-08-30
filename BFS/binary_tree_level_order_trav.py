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

    
    def levelOrderDoubleQueue(self, root: TreeNode) -> list:
        if root == None:
            return []

        even_q = []
        odd_q = []
        level_traversal = []
        traversal = []
        even_q.append(root)

        while len(even_q) > 0 or len(odd_q) > 0:
            if len(odd_q) == 0:
                while len(even_q) > 0:
                    node = even_q.pop(0)
                    level_traversal.append(node.val)

                    if node.left:
                        odd_q.append(node.left)

                    if node.right:
                        odd_q.append(node.right)
                if len(level_traversal) > 0:
                    traversal.append(level_traversal)
                    level_traversal = []
            

            if len(even_q) == 0:
                while len(odd_q) > 0:
                    node = odd_q.pop(0)
                    level_traversal.append(node.val)

                    if node.left:
                        even_q.append(node.left)

                    if node.right:
                        even_q.append(node.right)

                if len(level_traversal) > 0:               
                    traversal.append(level_traversal)
                    level_traversal = []


        return traversal