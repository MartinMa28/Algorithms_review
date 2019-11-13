from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def _preorder(self, root):
        if root == None:
            return 'X,'
        else:
            return '{},'.format(root.val) + \
                    self._preorder(root.left) + \
                    self._preorder(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        return self._preorder(root)[:-1]

    
    def _build_nodes(self, queue):
        """
        Deserialize the tree in the same order (preorder) as the serialzation.
        """
        popped = queue.popleft()
        if popped == 'X':
            return None
        node = TreeNode(int(popped))
        node.left = self._build_nodes(queue)
        node.right = self._build_nodes(queue)

        return node
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = deque(data.split(','))
        
        return self._build_nodes(q)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))