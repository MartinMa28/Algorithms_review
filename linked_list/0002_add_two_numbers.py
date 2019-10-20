# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def _parse_num(self, head: ListNode, pow: int) -> int:
        if head == None:
            return 0
        else:
            return head.val * (10 ** pow) + self._parse_num(head.next, pow + 1)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self._parse_num(l1, 0)
        num2 = self._parse_num(l2, 0)
        
        res = num1 + num2
        
        if res == 0:
            return ListNode(0)
    
        res_list = ListNode(-1)
        head = res_list
        
        while res > 0:
            head.next = ListNode(res % 10)
            head = head.next
            res = res // 10
            
        return res_list.next