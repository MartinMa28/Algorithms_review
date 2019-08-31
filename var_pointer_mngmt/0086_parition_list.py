class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        greater_header = ListNode(99999)
        less_header = ListNode(-99999)
        greater = greater_header
        less = less_header

        if head == None:
            return head
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        # concatenate less and greater
        greater.next = None
        less.next = greater_header.next

        return less_header.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    solu = Solution()
    re = solu.partition(head, 3)