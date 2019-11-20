# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def __init__(self):
#         self.cnt = 0
    
#     def _check_univalue(self, root, val) -> bool:
#         is_univalue = True
#         stack = [root]
        
#         while len(stack) > 0:
#             popped = stack.pop()
            
#             if popped.val != val:
#                 is_univalue = False
#                 break
            
#             if popped.right:
#                 stack.append(popped.right)
            
#             if popped.left:
#                 stack.append(popped.left)
        
#         return is_univalue
    
#     def _dfs(self, root: TreeNode) -> None:
#         if root:
#             if self._check_univalue(root, root.val):
#                 self.cnt += 1
                
#             self._dfs(root.left)
#             self._dfs(root.right)
    
#     def countUnivalSubtrees(self, root: TreeNode) -> int:
#         self._dfs(root)
        
#         return self.cnt

class Solution:
    def __init__(self):
        self.cnt = 0
    
    def _bottom_up(self, root) -> bool:
        if root.left == None and root.right == None:
            # leaf node
            self.cnt += 1
            return True
        
        is_univalue = True
        
        if root.left:
            is_univalue = self._bottom_up(root.left) and is_univalue and root.val == root.left.val
        
        if root.right:
            is_univalue = self._bottom_up(root.right) and is_univalue and root.val == root.right.val
            
        self.cnt += is_univalue
        return is_univalue
    
    def _is_uni(self, root) -> bool:
        if root.left == None and root.right == None:
            # leaf node is univalue
            self.uni_cnt += 1
            return True
        
        elif root.right == None:
            if self._is_uni(root.left) and root.val == root.left.val:
                self.uni_cnt += 1
                return True
            else:
                return False
    
        elif root.left == None:
            if self._is_uni(root.right) and root.val == root.right.val:
                self.uni_cnt += 1
                return True
            else:
                return False
            
        else:
            left_uni = self._is_uni(root.left)
            right_uni = self._is_uni(root.right)
            if left_uni and\
                right_uni and\
                root.val == root.left.val and\
                root.val == root.right.val:
                self.uni_cnt += 1
                return True
            else:
                return False

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self._bottom_up(root)
        
        return self.cnt