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
        # get rid of None in lists
        lists = filter(lambda l: l, lists)
        
        res_list = ListNode(777)
        head = res_list
        cnt = count()
        heap = [(l.val, next(cnt), l) for l in lists]
        
        heapq.heapify(heap)
        
        while len(heap) > 0:
            node_val, _, popped_list = heapq.heappop(heap)
            head.next = ListNode(node_val)
            head = head.next
            if popped_list.next:
                heapq.heappush(heap, (popped_list.next.val, next(cnt), popped_list.next))
                
        return res_list.next
                

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
        print(merged.val, end=' ')
        merged = merged.next

    print()


