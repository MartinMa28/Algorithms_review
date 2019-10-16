class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    def _find_min(self, root: TreeNode) -> TreeNode:
        if root.left:
            return self._find_min(root.left)
        else:
            return root


    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

            return root
        else:
            if root.left == None and root.right == None:
                return None
            elif root.left and root.right == None:
                return root.left
            elif root.right and root.left == None:
                return root.right
            else:
                # The target node has left and right child at the same time.
                min_node = self._find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

                return root
                # min_parent = root
                # min_node = root.right
                # while min_node.left:
                #     min_node = min_node.left
                #     min_parent = min_node

                # if min_parent != root:
                #     min_parent.left = min_node.right
                #     min_node.left = root.left
                #     min_node.right = root.right
                # else:
                #     min_node.left = root.left

                # return min_node