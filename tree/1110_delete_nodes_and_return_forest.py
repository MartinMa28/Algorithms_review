class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _del_nodes(self, root: TreeNode, to_delete: set) -> list:
        if root:
            res = []
            
            root.left, left_forest = self._del_nodes(root.left, to_delete)
            root.right, right_forest = self._del_nodes(root.right, to_delete)
                
            if root.val in to_delete:
                res.extend(left_forest)
                res.extend(right_forest)
                
                return None, res
            else:
                left_forest = filter(lambda x: x is not root.left, left_forest)
                right_forest = filter(lambda x: x is not root.right, right_forest)
                
                res.extend(left_forest)
                res.extend(right_forest)
                res.append(root)
                
                return root, res
        else:
            return None, []
        
    def delNodes(self, root: TreeNode, to_delete: list) -> list:
        return self._del_nodes(root, set(to_delete))[1]