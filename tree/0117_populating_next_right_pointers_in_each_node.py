from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        odd_q = deque()
        even_q = deque()
        
        odd_q.append(root)
        
        while len(odd_q) > 0 or len(even_q) > 0:
            prev_node = None
            if len(odd_q) > 0:
                while len(odd_q) > 0:
                    popped = odd_q.popleft()
                    
                    if popped:
                        if prev_node:
                            prev_node.next = popped
                        prev_node = popped

                        even_q.append(popped.left)
                        even_q.append(popped.right)
            else:
                while len(even_q) > 0:
                    popped = even_q.popleft()
                    
                    if popped:
                        if prev_node:
                            prev_node.next = popped
                        prev_node = popped

                        odd_q.append(popped.left)
                        odd_q.append(popped.right)
                        
        return root