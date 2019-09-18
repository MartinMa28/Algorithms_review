class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        met = set()

        while headA:
            met.add(headA)
            headA = headA.next

        while headB:
            if headB in met:
                return headB
            else:
                headB = headB.next

        return None