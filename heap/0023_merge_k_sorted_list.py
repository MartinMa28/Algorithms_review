# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        min_heap = []
        cnt = 1
        for l in lists:
            if l:
                min_heap.append((l.val, cnt, l))
                cnt += 1
                
        heapq.heapify(min_heap)
        
        head = ListNode(-999)
        head_copy = head
        
        while len(min_heap) > 0:
            popped_val, _, popped = heapq.heappop(min_heap)
            node = ListNode(popped_val)
            head.next = node
            head = head.next
            
            if popped.next:
                heapq.heappush(min_heap, (popped.next.val, cnt, popped.next))
                cnt += 1
                
        return head_copy.next
        