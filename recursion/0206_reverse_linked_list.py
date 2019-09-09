class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        next_node = head.next
        head.next = None
        while next_node:
            next_next_node = next_node.next
            next_node.next = head
            head = next_node
            next_node = next_next_node

        return head
            

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        
        remaining = head.next
        head.next = None
        remaining = self.reverseList_recursive(remaining)

        cur = remaining
        while cur.next:
            cur = cur.next

        cur.next = head

        return remaining


if __name__ == "__main__":
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)

    solu = Solution()
    solu.reverseList_recursive(h)