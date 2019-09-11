class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head == None:
            return None
        
        og_to_dc = {}

        cur = head
        head_copy = Node(head.val, None, None)
        cur_copy = head_copy

        while cur:
            og_to_dc[cur] = cur_copy
            if cur.next:
                cur_copy.next = Node(cur.next.val, None, None)
            
            cur = cur.next
            cur_copy = cur_copy.next

        cur = head
        cur_copy = head_copy

        while cur:
            if cur.random:
                cur_copy.random = og_to_dc[cur.random]
            
            cur = cur.next
            cur_copy = cur_copy.next

        return head_copy
