class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        header = ListNode(999)
        header.next = head
        
        cur = header
        for i in range(m):
            if i == m - 1:
                start = cur.next
                before_start = cur
                cur.next = None
            else:
                cur = cur.next

        cur = start
        for i in range(n - m + 1):
            if i == n - m:
                end = cur.next
                cur.next = None
            else:
                cur = cur.next

        revd = self._reverse_sublist(start)
        before_start.next = revd

        cur = header
        while cur.next:
            cur = cur.next

        cur.next = end

        return header.next




    
    def _reverse_sublist(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        next_node = head.next
        head.next = None

        while next_node:
            further = next_node.next
            next_node.next = head
            head = next_node
            next_node = further

        return head


if __name__ == "__main__":
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)

    solu = Solution()
    solu.reverseBetween(h, 2, 4)