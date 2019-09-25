import heapq
from itertools import count


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __eq__(self, other):
    #     return self.val == other.val

    # def __ne__(self, other):
    #     return self.val != other.val

    # def __lt__(self, other):
    #     return self.val < other.val

    # def __gt__(self, other):
    #     return self.val > other.val

    # def __le__(self, other):
    #     return self.val <= other.val

    # def __ge__(self, other):
    #     return self.val >= other.val



class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        if lists == []:
            return None
        
        # min heap q
        hq = []
        cnt = count(0)
        for list_node in lists:
            if list_node:
                heapq.heappush(hq, (list_node.val, next(cnt), list_node))

        head = ListNode(-999)
        head_copy = head

        while len(hq) > 0:
            min_node = heapq.heappop(hq)
            
            head.next = min_node[2]
            if min_node[2].next:
                heapq.heappush(hq, (min_node[2].next.val, next(cnt), min_node[2].next))
            head = head.next

        return  head_copy.next
                

if __name__ == "__main__":
    l01 = ListNode(1)
    l04 = ListNode(4)
    l05 = ListNode(5)
    l11 = ListNode(1)
    l13 = ListNode(3)
    l14 = ListNode(4)
    l22 = ListNode(2)
    l26 = ListNode(6)

    l01.next = l04
    l04.next = l05

    l11.next = l13
    l13.next = l14

    l22.next = l26

    solu = Solution()
    
    merged = solu.mergeKLists([l01, l11, l22])
    
    while merged.next:
        print(merged.val)
        merged = merged.next


