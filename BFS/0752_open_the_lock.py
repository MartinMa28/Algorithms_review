from collections import deque

class Solution:
    
    def _next_move(self, lock):
        for i in range(4):
            x = int(lock[i])
            for d in (1, -1):
                y = (x + d) % 10
                yield lock[:i] + str(y) + lock[i + 1:]
       
    
    def openLock(self, deadends: list, target: str) -> int:
        initial = '0000'
        
        deadends = set(deadends)
        queue = deque()
        queue.append((initial, 0))
        visited = set()
        visited.add(initial)
        
        while len(queue) > 0:
            popped, cnt = queue.popleft()
            if popped == target:
                return cnt
            elif popped in deadends:
                continue
            else:
                for status in self._next_move(popped):
                    if status not in visited:
                        visited.add(status)
                        queue.append((status, cnt + 1))
                               
        return -1
        
        

if __name__ == "__main__":
    solu = Solution()
    print(solu.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888'))