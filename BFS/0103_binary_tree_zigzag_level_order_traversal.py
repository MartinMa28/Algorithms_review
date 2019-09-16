from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzaglevelOrder(self, root: TreeNode) -> list:
        queue = deque()
        stack = []
        left_to_right = True
        res = []

        if root == None:
            return []

        queue.append(root)

        while len(queue) > 0:
            level_trav = []
            while len(queue) > 0:
                popped = queue.popleft()
                level_trav.append(popped.val)
                stack.append(popped)

            res.append(level_trav)
            
            while len(stack) > 0:
                popped = stack.pop(-1)
                if left_to_right:
                    # left to right in current iteration,
                    # so right to left in the next
                    if popped.right:
                        queue.append(popped.right)
                    if popped.left:
                        queue.append(popped.left)
                else:
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
            
            left_to_right = not left_to_right

        return res

