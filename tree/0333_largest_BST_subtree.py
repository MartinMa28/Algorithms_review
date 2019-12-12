# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.largest = -1
    
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self._largest_BST(root)
        
        return max((self.largest, 0))
    
    def _largest_BST(self, root: TreeNode):
        if root == None:
            return root, root, 0
        else:
            left_max, left_min, l_cnt = self._largest_BST(root.left)
            right_max, right_min, r_cnt = self._largest_BST(root.right)
            
            if l_cnt == -1 or r_cnt == -1:
                return None, None, -1
            else:
                if left_max and right_min:
                    if root.val > left_max.val and root.val < right_min.val:
                        self.largest = max((self.largest, l_cnt + r_cnt + 1))
                        return right_max, left_min, l_cnt + r_cnt + 1
                    else:
                        return right_max, left_min, -1
                elif left_max:
                    if root.val > left_max.val:
                        self.largest = max((self.largest, l_cnt + 1))
                        return root, left_min, l_cnt + 1
                    else:
                        return None, None, -1
                elif right_min:
                    if root.val < right_min.val:
                        self.largest = max((self.largest, r_cnt + 1))
                        return right_max, root, r_cnt + 1
                    else:
                        return None, None, -1
                else:
                    self.largest = max((self.largest, 1))
                    return root, root, 1