class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        elif head.next == None:
            return head
        else:
            new_head = head.next
            next_head = head.next.next
            new_head.next = head
            new_head.next.next = self.swapPairs(next_head)

            return new_head

