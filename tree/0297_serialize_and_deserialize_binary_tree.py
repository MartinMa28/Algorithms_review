from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.enc = []
        
    def _preorder(self, root):
        if root:
            self.enc.append(root.val)
            self._preorder(root.left)
            self._preorder(root.right)
        else:
            self.enc.append(None)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.enc = []
        self._preorder(root)
        
        return ','.join(map(lambda x: str(x), self.enc))

    
    def _deserialize(self, queue):
        popped = queue.popleft()
        
        if popped == 'None':
            return None
        else:
            root = TreeNode(int(popped))
            root.left = self._deserialize(queue)
            root.right = self._deserialize(queue)
            
            return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        enc = deque(data.split(','))
        
        return self._deserialize(enc)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))