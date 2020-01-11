"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            flattened_child = self.flatten(head.child)
            flattened_next = self.flatten(head.next)
            
            cur = head
            cur.child = None
            
            if flattened_child:
                cur.next = flattened_child
                flattened_child.prev = cur
                
                while cur.next:
                    cur = cur.next
                    
            cur.next = flattened_next
            if flattened_next:
                flattened_next.prev = cur
        
        return head