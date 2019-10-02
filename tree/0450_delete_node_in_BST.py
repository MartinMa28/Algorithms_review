class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _minimum(self, root) -> tuple:
        """
        find the minimum node below root (the left most child)
        return a tuple (min_node, min_node' parent)
        """
        parent = None
        x = root

        while x:
            if x.left:
                parent = x
                x = x.left
            else:
                break

        return (x, parent)


    def _search(self, root, key: int) -> tuple:
        """
        search the node whose val equals key
        return a tuple (node, node's parent)
        """
        parent = None
        x = root
        
        while x:
            if x.val == key:
                return (x, parent)
            elif x.val > key:
                parent = x
                x = x.left
            else:
                parent = x
                x = x.right

        return (None, None)


    def _transplant(self, root: TreeNode,
                            u: TreeNode,
                            u_par: TreeNode,
                            v: TreeNode) -> TreeNode:
        """
        Replace u with v. In other words, u's parent becomes v'parent.
        And we don't care where is u.
        """
        if u_par is None:
            # Special case: u is the root, it doesn't have parent.
            root = v
        else:
            if u is u_par.left:
                u_par.left = v
            else:
                u_par.right = v
        
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        node, parent = self._search(root, key)
        
        if node is None:
            # Not found, so nothing to delete.
            return root

        if node.left is None:
            root = self._transplant(root, node, parent, node.right)
        elif node.right is None:
            root = self._transplant(root, node, parent, node.left)
        else:
            # Firstly, find the minimum node of the node's right sub-tree.
            min_node, min_node_par = self._minimum(node.right)

            if min_node is not node.right:
                # If min_node is not the right child of the deleting target node,
                # Let the min_node's right child replace min_node.
                # Note that min_node doesn't have left child.
                # And then, let deleting target's right child be the min_node's right child.
                root = self._transplant(root, min_node, min_node_par, min_node.right)
                min_node.right = node.right

            # Simply replace deleting target node with min_node.
            root = self._transplant(root, node, parent, min_node)
            # Let the deleting target node's left child be the min_node's left child.
            min_node.left = node.left
        
        return root

            
if __name__ == "__main__":
    r = TreeNode(3)
    ri = TreeNode(4)
    le = TreeNode(1)
    lr = TreeNode(2)
    r.right = ri
    r.left = le
    r.left.right = lr

    solu = Solution()
    solu.deleteNode(r, 3)
    