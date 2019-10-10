# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _is_mirror(self, left, right):
        if left == None and right == None:
            return True
        elif (left == None and right) or (left and right == None):
            return False
        else:
            return left.val == right.val and self._is_mirror(left.left, right.right) and self._is_mirror(left.right, right.left)
    
    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self._is_mirror(root.left, root.right)

    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        odd_q = []
        even_q = []

        odd_q.append(root)
        traverse = []
        
        while len(odd_q) > 0 or len(even_q) > 0:
            level = []
            if len(odd_q) > 0:
                while len(odd_q) > 0:
                    node = odd_q.pop()
                    if node:
                        level.append(node.val)
                        even_q.append(node.left)
                        even_q.append(node.right)
            
            if len(even_q) > 0:
                while len(even_q) > 0:
                    node = even_q.pop()
                    if node:
                        level.append(node.val)
                        odd_q.append(node.left)
                        odd_q.append(node.right)

            for i in range(len(level) // 2):
                if level[i] != level[-i - 1]:
                    return False

        
        return True

if __name__ == "__main__":
    solu = Solution()
    solu.isSymmetric_iterative()


                

