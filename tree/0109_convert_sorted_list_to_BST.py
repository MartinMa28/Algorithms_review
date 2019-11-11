# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def _build_bst(self, in_order):
        if in_order == []:
            return None
        
        mid = len(in_order) >> 1
        node = TreeNode(in_order[mid])
        node.left = self._build_bst(in_order[:mid])
        node.right = self._build_bst(in_order[mid + 1:])
        
        return node
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # convert linked list to array
        node_arr = []
        while head:
            node_arr.append(head.val)
            head = head.next
            
        return self._build_bst(node_arr)