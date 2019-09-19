from collections import deque

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def _level_order_trav(self, root) -> list:
        odd_queue = deque()
        even_queue = deque()
        level_trav = []
        odd_queue.append(root)

        while len(odd_queue) > 0 or len(even_queue) > 0:
            cur_level = []
            if len(odd_queue) > 0:
                while len(odd_queue) > 0:
                    popped = odd_queue.popleft()
                    if popped:
                        cur_level.append(popped)
                        even_queue.append(popped.left)
                        even_queue.append(popped.right)
            else:
                while len(even_queue) > 0:
                    popped = even_queue.popleft()
                    if popped:
                        cur_level.append(popped)
                        odd_queue.append(popped.left)
                        odd_queue.append(popped.right)

            if cur_level != []:
                level_trav.append(cur_level)
        
        return level_trav


    def connect(self, root: Node) -> Node:
        if root == None:
            return None
            
        level_trav = self._level_order_trav(root)
        
        for level in level_trav:
            if len(level) > 1:
                for i in range(len(level) - 1):
                    level[i].next = level[i + 1]

        return level_trav[0][0]


if __name__ == "__main__":
    solu = Solution()
    n7 = Node(7, None, None, None)
    n6 = Node(6, None, None, None)
    n3 = Node(3, n6, n7, None)
    n5 = Node(5, None, None, None)
    n4 = Node(4, None, None, None)
    n2 = Node(2, n4, n5, None)
    n1 = Node(1, n2, n3, None)

    solu.connect(n1)