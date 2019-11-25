# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.max_path_sum = -float('inf')
    
    
    def _max_path_sum(self, root):
        if root == None:
            return 0
        
        left_path_sum = self._max_path_sum(root.left)
        right_path_sum = self._max_path_sum(root.right)
        
        self.max_path_sum = max((self.max_path_sum, root.val + left_path_sum + right_path_sum, max((left_path_sum, right_path_sum)) + root.val, root.val))
        
        if max((left_path_sum, right_path_sum)) > 0:
            return max((left_path_sum, right_path_sum)) + root.val
        else:
            return root.val
        
    
    def maxPathSum(self, root: TreeNode) -> int:
        self._max_path_sum(root)
        return self.max_path_sum


if __name__ == "__main__":
    solu = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right= n3

    print(solu.maxPathSum(n1))