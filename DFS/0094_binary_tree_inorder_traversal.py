class TreeNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> list:
        if root == None:
            return []
        
        stack = []
        visited = set()
        trav = []

        stack.append(root)

        while len(stack) > 0:
            if stack[-1].left and stack[-1].left not in visited:
                # check the left child
                stack.append(stack[-1].left)
            else:
                # no left child or left child has been visited
                popped = stack.pop()
                trav.append(popped.val)
                visited.add(popped)

                # if has right child, visit it
                if popped.right:
                    stack.append(popped.right)

        return trav