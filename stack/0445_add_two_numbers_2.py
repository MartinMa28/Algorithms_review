# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    @staticmethod
    def _build_list(stack):
        head = ListNode(-777)
        cur = head
        
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
            
        return head.next
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        stack_res = []
        
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
        
        if len(stack_1) < len(stack_2):
            stack_1, stack_2 = stack_2, stack_1
        
        carry = 0
        while stack_1 and stack_2:
            op_1 = stack_1.pop()
            op_2 = stack_2.pop()
            
            stack_res.append((op_1 + op_2 + carry) % 10)
            carry = (op_1 + op_2 + carry) // 10
            
        while stack_1:
            op = stack_1.pop()
            
            stack_res.append((op + carry) % 10)
            carry = (op + carry) // 10
        
        if carry:
            stack_res.append(carry)
        
        return self._build_list(stack_res)