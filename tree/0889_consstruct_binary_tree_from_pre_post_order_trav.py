# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def _pre_pre(self, pre, rev_pre):
        if pre and rev_pre:
            root = TreeNode(pre[0])
            
            if len(pre) == 1 and len(rev_pre) == 1:
                return root
            elif pre[1] == rev_pre[1]:
                root.left = self._pre_pre(pre[1:], rev_pre[1:])
                return root
            else:
                left_val = pre[1]
                right_val = rev_pre[1]
                
                pre_bound = -1
                rev_pre_bound = -1
                
                for i in range(len(pre)):
                    if pre[i] == right_val:
                        pre_bound = i
                        break
                        
                for i in range(len(rev_pre)):
                    if rev_pre[i] == left_val:
                        rev_pre_bound = i
                        break
                        
                left_pre = pre[1:pre_bound]
                right_pre = pre[pre_bound:]
                right_rev_pre = rev_pre[1:rev_pre_bound]
                left_rev_pre = rev_pre[rev_pre_bound:]
                
                root.left = self._pre_pre(left_pre, left_rev_pre)
                root.right = self._pre_pre(right_pre, right_rev_pre)
                
                return root
        else:
            return None
    
    def constructFromPrePost(self, pre: list, post: list) -> TreeNode:
        return self._pre_pre(pre, post[-1::-1])
        
        